"""
Phase 1: Build PP-GMM input time series.

For each student with adaptive_ratio >= 0.10:
1. Parse all episodes from raw KT3 file
2. Split into 10 non-overlapping windows (deciles)
3. Compute per-window: R_b, P, and auxiliary variables
4. Output long-format CSV for R (lcmm::multlcmm)

Outputs:
  - phase1_timeseries_long.csv   (long format for R: student_id, time, R_b, P)
  - phase1_student_summary.csv   (per-student summary: demographics, totals)
  - phase1_early_behavior.csv    (first-decile features for RQ3 prediction)
"""

import csv
import time
import statistics
from pathlib import Path
from concurrent.futures import ProcessPoolExecutor, as_completed

RAW_DIR = Path("/Volumes/External SSD/Projects/Research/Trust-Calibration-Scaffolds-research/"
               "TCR-Trajectory-Paper/data/ednet-kt3/raw/KT3")
PROC_DIR = Path("/Volumes/External SSD/Projects/Research/Trust-Calibration-Scaffolds-research/"
                "TCR-Trajectory-Paper/data/ednet-kt3/processed")
META_DIR = Path("/Volumes/External SSD/Projects/Research/Trust-Calibration-Scaffolds-research/"
                "TCR-Trajectory-Paper/data/ednet-kt3/metadata")
OUT_DIR = Path("/Volumes/External SSD/Projects/Research/Trust-Calibration-Scaffolds-research/"
               "TCR-Trajectory-Paper/analysis/outputs")

N_WINDOWS = 10
ADAPTIVE_RATIO_THRESHOLD = 0.10

CORRECT_ANSWERS = None


def _init_worker(answers_dict):
    global CORRECT_ANSWERS
    CORRECT_ANSWERS = answers_dict


def load_correct_answers():
    answers = {}
    with open(META_DIR / "questions.csv", "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            answers[row["question_id"]] = row["correct_answer"]
    return answers


def process_student(user_id: str) -> dict:
    """Parse episodes, compute windowed time series, extract early behavior."""
    filepath = RAW_DIR / f"{user_id}.csv"

    # --- Parse episodes ---
    episodes = []
    current = None

    with open(filepath, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            action = row.get("action_type", "")
            item_id = row.get("item_id", "")
            src = row.get("source", "")
            ts = int(row.get("timestamp", 0))
            answer = row.get("user_answer", "")
            platform = row.get("platform", "")

            if action == "enter" and item_id.startswith("b"):
                if current is not None:
                    episodes.append(current)
                current = {
                    "timestamp": ts,
                    "source": src,
                    "is_adaptive": src == "adaptive_offer",
                    "bundle_id": item_id,
                    "correct": 0,
                    "total_q": 0,
                    "read_explanation": False,
                    "explanation_duration_ms": 0,
                    "watched_lecture": False,
                    "lecture_duration_ms": 0,
                    "answer_changes": 0,
                    "platform": platform,
                    "responded_questions": set(),
                }
            elif action == "respond" and current is not None:
                q_id = item_id
                correct_ans = CORRECT_ANSWERS.get(q_id, "")
                is_correct = answer == correct_ans if correct_ans else False
                if q_id in current["responded_questions"]:
                    current["answer_changes"] += 1
                else:
                    current["total_q"] += 1
                    if is_correct:
                        current["correct"] += 1
                    current["responded_questions"].add(q_id)
            elif action == "enter" and item_id.startswith("e") and current is not None:
                current["read_explanation"] = True
                current["_expl_enter_ts"] = ts
            elif action == "quit" and item_id.startswith("e") and current is not None:
                enter_ts = current.get("_expl_enter_ts", 0)
                if enter_ts > 0:
                    current["explanation_duration_ms"] = ts - enter_ts
            elif action == "enter" and item_id.startswith("l") and current is not None:
                current["watched_lecture"] = True
                current["_lect_enter_ts"] = ts
            elif action == "quit" and item_id.startswith("l") and current is not None:
                enter_ts = current.get("_lect_enter_ts", 0)
                if enter_ts > 0:
                    current["lecture_duration_ms"] = ts - enter_ts

    if current is not None:
        episodes.append(current)

    # Clean up temporary fields
    for ep in episodes:
        ep.pop("responded_questions", None)
        ep.pop("_expl_enter_ts", None)
        ep.pop("_lect_enter_ts", None)

    n_episodes = len(episodes)
    if n_episodes < N_WINDOWS:
        return None

    # --- Compute windows ---
    window_size = n_episodes // N_WINDOWS
    windows = []

    for w in range(N_WINDOWS):
        start = w * window_size
        end = start + window_size if w < N_WINDOWS - 1 else n_episodes
        win_eps = episodes[start:end]

        n_eps = len(win_eps)
        n_adaptive = sum(1 for e in win_eps if e["is_adaptive"])
        total_q = sum(e["total_q"] for e in win_eps)
        total_correct = sum(e["correct"] for e in win_eps)
        n_explanation = sum(1 for e in win_eps if e["read_explanation"])
        total_expl_dur = sum(e["explanation_duration_ms"] for e in win_eps)
        n_lecture = sum(1 for e in win_eps if e["watched_lecture"])
        n_answer_change = sum(e["answer_changes"] for e in win_eps)

        r_b = n_adaptive / n_eps if n_eps > 0 else 0.0
        p = total_correct / total_q if total_q > 0 else 0.0
        expl_rate = n_explanation / n_eps if n_eps > 0 else 0.0
        avg_expl_dur = (total_expl_dur / n_explanation / 1000) if n_explanation > 0 else 0.0  # seconds
        lecture_rate = n_lecture / n_eps if n_eps > 0 else 0.0
        change_rate = n_answer_change / n_eps if n_eps > 0 else 0.0

        windows.append({
            "user_id": user_id,
            "window": w + 1,  # 1-indexed
            "n_episodes": n_eps,
            "n_adaptive": n_adaptive,
            "n_questions": total_q,
            "n_correct": total_correct,
            "R_b": round(r_b, 6),
            "P": round(p, 6),
            "gap": round(r_b - p, 6),
            "expl_rate": round(expl_rate, 6),
            "avg_expl_dur_s": round(avg_expl_dur, 2),
            "lecture_rate": round(lecture_rate, 6),
            "answer_change_rate": round(change_rate, 6),
        })

    # --- Student summary ---
    total_adaptive = sum(e["is_adaptive"] for e in episodes)
    total_q_all = sum(e["total_q"] for e in episodes)
    total_correct_all = sum(e["correct"] for e in episodes)
    time_span_ms = episodes[-1]["timestamp"] - episodes[0]["timestamp"] if len(episodes) > 1 else 0
    platforms = set(e["platform"] for e in episodes)

    summary = {
        "user_id": user_id,
        "n_episodes": n_episodes,
        "n_adaptive": total_adaptive,
        "adaptive_ratio": round(total_adaptive / n_episodes, 6),
        "n_questions": total_q_all,
        "n_correct": total_correct_all,
        "overall_accuracy": round(total_correct_all / total_q_all, 6) if total_q_all > 0 else 0,
        "time_span_days": round(time_span_ms / (1000 * 3600 * 24), 2),
        "platforms": ";".join(sorted(platforms)),
        "window_size": window_size,
    }

    # --- Early behavior (first window) for RQ3 ---
    first_win = windows[0]
    early = {
        "user_id": user_id,
        "early_R_b": first_win["R_b"],
        "early_P": first_win["P"],
        "early_gap": first_win["gap"],
        "early_expl_rate": first_win["expl_rate"],
        "early_avg_expl_dur_s": first_win["avg_expl_dur_s"],
        "early_lecture_rate": first_win["lecture_rate"],
        "early_answer_change_rate": first_win["answer_change_rate"],
        "early_n_episodes": first_win["n_episodes"],
    }

    return {"windows": windows, "summary": summary, "early": early}


def main():
    global CORRECT_ANSWERS
    print("Loading correct answers...")
    CORRECT_ANSWERS = load_correct_answers()
    print(f"  {len(CORRECT_ANSWERS):,} questions loaded")

    # Load target students (adaptive ratio >= 0.10)
    depth_path = PROC_DIR / "phase0_2_episode_depth.csv"
    target_students = []
    with open(depth_path, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if (float(row["adaptive_ratio"]) >= ADAPTIVE_RATIO_THRESHOLD
                and int(row["total_episodes"]) >= 60
                and int(row["adaptive_episodes"]) >= 5
                and float(row["time_span_days"]) >= 1):
                target_students.append(row["user_id"])

    print(f"Target students (ratio ≥ {ADAPTIVE_RATIO_THRESHOLD}): {len(target_students):,}")

    # Process
    all_windows = []
    all_summaries = []
    all_early = []
    start = time.time()

    with ProcessPoolExecutor(max_workers=8, initializer=_init_worker, initargs=(CORRECT_ANSWERS,)) as executor:
        futures = {executor.submit(process_student, uid): uid for uid in target_students}
        done = 0
        skipped = 0
        for future in as_completed(futures):
            result = future.result()
            if result is None:
                skipped += 1
            else:
                all_windows.extend(result["windows"])
                all_summaries.append(result["summary"])
                all_early.append(result["early"])
            done += 1
            if done % 1000 == 0:
                elapsed = time.time() - start
                rate = done / elapsed
                eta = (len(target_students) - done) / rate if rate > 0 else 0
                print(f"  {done:,}/{len(target_students):,} - {rate:.0f}/s - ETA {eta:.0f}s")

    elapsed = time.time() - start
    print(f"\nProcessed: {len(all_summaries):,} students ({skipped} skipped) in {elapsed:.1f}s")

    # Sort
    all_windows.sort(key=lambda x: (x["user_id"], x["window"]))
    all_summaries.sort(key=lambda x: x["user_id"])
    all_early.sort(key=lambda x: x["user_id"])

    # Ensure output directory exists
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    # Save time series (long format)
    ts_path = OUT_DIR / "phase1_timeseries_long.csv"
    ts_fields = [
        "user_id", "window", "n_episodes", "n_adaptive", "n_questions",
        "n_correct", "R_b", "P", "gap", "expl_rate", "avg_expl_dur_s",
        "lecture_rate", "answer_change_rate"
    ]
    with open(ts_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=ts_fields)
        writer.writeheader()
        writer.writerows(all_windows)
    print(f"Saved: {ts_path} ({len(all_windows):,} rows)")

    # Save student summary
    sum_path = OUT_DIR / "phase1_student_summary.csv"
    sum_fields = [
        "user_id", "n_episodes", "n_adaptive", "adaptive_ratio",
        "n_questions", "n_correct", "overall_accuracy",
        "time_span_days", "platforms", "window_size"
    ]
    with open(sum_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=sum_fields)
        writer.writeheader()
        writer.writerows(all_summaries)
    print(f"Saved: {sum_path} ({len(all_summaries):,} rows)")

    # Save early behavior
    early_path = OUT_DIR / "phase1_early_behavior.csv"
    early_fields = [
        "user_id", "early_R_b", "early_P", "early_gap",
        "early_expl_rate", "early_avg_expl_dur_s",
        "early_lecture_rate", "early_answer_change_rate", "early_n_episodes"
    ]
    with open(early_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=early_fields)
        writer.writeheader()
        writer.writerows(all_early)
    print(f"Saved: {early_path} ({len(all_early):,} rows)")

    # --- Summary statistics ---
    print(f"\n{'='*60}")
    print(f"PHASE 1 SUMMARY")
    print(f"{'='*60}")
    print(f"Students: {len(all_summaries):,}")
    print(f"Windows per student: {N_WINDOWS}")
    print(f"Total window-observations: {len(all_windows):,}")

    # R_b across all windows
    rb_vals = [w["R_b"] for w in all_windows]
    p_vals = [w["P"] for w in all_windows]
    gap_vals = [w["gap"] for w in all_windows]

    print(f"\nR_b (Reliance):")
    print(f"  Mean={statistics.mean(rb_vals):.4f}, Median={statistics.median(rb_vals):.4f}, "
          f"Std={statistics.stdev(rb_vals):.4f}")
    n_zero = sum(1 for v in rb_vals if v == 0)
    print(f"  Zero: {n_zero:,}/{len(rb_vals):,} ({n_zero/len(rb_vals)*100:.1f}%)")

    print(f"\nP (Performance):")
    print(f"  Mean={statistics.mean(p_vals):.4f}, Median={statistics.median(p_vals):.4f}, "
          f"Std={statistics.stdev(p_vals):.4f}")

    print(f"\nGap (R_b - P):")
    print(f"  Mean={statistics.mean(gap_vals):.4f}, Median={statistics.median(gap_vals):.4f}, "
          f"Std={statistics.stdev(gap_vals):.4f}")

    # Per-window means
    print(f"\nPer-window means:")
    print(f"  {'Window':>6} {'R_b':>8} {'P':>8} {'Gap':>8} {'%zero_Rb':>10}")
    for w in range(1, N_WINDOWS + 1):
        w_rb = [x["R_b"] for x in all_windows if x["window"] == w]
        w_p = [x["P"] for x in all_windows if x["window"] == w]
        w_gap = [x["gap"] for x in all_windows if x["window"] == w]
        pct_zero = sum(1 for v in w_rb if v == 0) / len(w_rb) * 100 if w_rb else 0
        print(f"  {w:>6} {statistics.mean(w_rb):>8.4f} {statistics.mean(w_p):>8.4f} "
              f"{statistics.mean(w_gap):>8.4f} {pct_zero:>9.1f}%")

    # Student-level summary
    accuracies = [s["overall_accuracy"] for s in all_summaries]
    ratios = [s["adaptive_ratio"] for s in all_summaries]
    spans = [s["time_span_days"] for s in all_summaries]
    eps = [s["n_episodes"] for s in all_summaries]

    print(f"\nStudent-level:")
    print(f"  Episodes:  median={statistics.median(eps):.0f}, mean={statistics.mean(eps):.1f}")
    print(f"  Accuracy:  median={statistics.median(accuracies):.4f}, mean={statistics.mean(accuracies):.4f}")
    print(f"  Ad. ratio: median={statistics.median(ratios):.4f}, mean={statistics.mean(ratios):.4f}")
    print(f"  Time span: median={statistics.median(spans):.1f}d, mean={statistics.mean(spans):.1f}d")


if __name__ == "__main__":
    main()
