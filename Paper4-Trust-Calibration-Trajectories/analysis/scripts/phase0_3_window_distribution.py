"""
Phase 0-3: Window-level R_b and P distribution analysis.

For a sample of GMM-ready students, compute actual R_b and P values
in 20 non-overlapping windows (ventiles) to assess:
1. R_b zero-inflation per window
2. R_b and P variance (enough signal for GMM?)
3. R_b × P correlation structure

Uses a random sample of 2,000 students for speed.
"""

import csv
import random
import time
import statistics
from pathlib import Path
from collections import defaultdict
from concurrent.futures import ProcessPoolExecutor, as_completed

RAW_DIR = Path("/Volumes/External SSD/Projects/Research/Trust-Calibration-Scaffolds-research/TCR-Trajectory-Paper/data/ednet-kt3/raw/KT3")
PROC_DIR = Path("/Volumes/External SSD/Projects/Research/Trust-Calibration-Scaffolds-research/TCR-Trajectory-Paper/data/ednet-kt3/processed")
META_DIR = Path("/Volumes/External SSD/Projects/Research/Trust-Calibration-Scaffolds-research/TCR-Trajectory-Paper/data/ednet-kt3/metadata")

N_WINDOWS = 20
SAMPLE_SIZE = 2000

# Load correct answers
def load_correct_answers():
    answers = {}
    with open(META_DIR / "questions.csv", "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            answers[row["question_id"]] = row["correct_answer"]
    return answers

CORRECT_ANSWERS = None


def _init_worker(answers_dict):
    """Initialize worker process with shared data."""
    global CORRECT_ANSWERS
    CORRECT_ANSWERS = answers_dict


def compute_windows(user_id: str) -> list:
    """Parse episodes, split into ventiles, compute R_b and P per window."""
    filepath = RAW_DIR / f"{user_id}.csv"

    # Parse episodes
    episodes = []
    current_episode = None

    with open(filepath, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            action = row.get("action_type", "")
            item_id = row.get("item_id", "")
            src = row.get("source", "")
            ts = int(row.get("timestamp", 0))
            answer = row.get("user_answer", "")

            if action == "enter" and item_id.startswith("b"):
                if current_episode is not None:
                    episodes.append(current_episode)
                current_episode = {
                    "timestamp": ts,
                    "source": src,
                    "is_adaptive": src == "adaptive_offer",
                    "questions": [],
                    "correct": 0,
                    "total_q": 0,
                }
            elif action == "respond" and current_episode is not None:
                q_id = item_id
                correct_ans = CORRECT_ANSWERS.get(q_id, "")
                is_correct = answer == correct_ans if correct_ans else False
                current_episode["questions"].append({
                    "q_id": q_id,
                    "answer": answer,
                    "correct": is_correct,
                })
                current_episode["total_q"] += 1
                if is_correct:
                    current_episode["correct"] += 1

        if current_episode is not None:
            episodes.append(current_episode)

    if len(episodes) < N_WINDOWS:
        return []

    # Split into N_WINDOWS ventiles
    window_size = len(episodes) // N_WINDOWS
    if window_size < 1:
        return []

    windows = []
    for w in range(N_WINDOWS):
        start = w * window_size
        end = start + window_size if w < N_WINDOWS - 1 else len(episodes)
        window_eps = episodes[start:end]

        n_eps = len(window_eps)
        n_adaptive = sum(1 for e in window_eps if e["is_adaptive"])
        total_correct = sum(e["correct"] for e in window_eps)
        total_questions = sum(e["total_q"] for e in window_eps)

        r_b = n_adaptive / n_eps if n_eps > 0 else 0
        p = total_correct / total_questions if total_questions > 0 else 0

        windows.append({
            "user_id": user_id,
            "window": w + 1,
            "n_episodes": n_eps,
            "n_adaptive": n_adaptive,
            "n_questions": total_questions,
            "n_correct": total_correct,
            "R_b": round(r_b, 4),
            "P": round(p, 4),
            "gap": round(r_b - p, 4),
        })

    return windows


def main():
    global CORRECT_ANSWERS
    print("Loading correct answers...")
    CORRECT_ANSWERS = load_correct_answers()
    print(f"  Loaded {len(CORRECT_ANSWERS):,} question answers")

    # Load GMM-ready students
    depth_path = PROC_DIR / "phase0_2_episode_depth.csv"
    gmm_ready = []
    with open(depth_path, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if (int(row["total_episodes"]) >= 60
                and int(row["adaptive_episodes"]) >= 5
                and float(row["time_span_days"]) >= 1):
                gmm_ready.append(row["user_id"])

    print(f"GMM-ready students: {len(gmm_ready):,}")

    # Random sample
    random.seed(42)
    sample = random.sample(gmm_ready, min(SAMPLE_SIZE, len(gmm_ready)))
    print(f"Sampling {len(sample):,} students for window analysis...")

    all_windows = []
    start = time.time()

    with ProcessPoolExecutor(max_workers=8, initializer=_init_worker, initargs=(CORRECT_ANSWERS,)) as executor:
        futures = {executor.submit(compute_windows, uid): uid for uid in sample}
        done = 0
        for future in as_completed(futures):
            windows = future.result()
            all_windows.extend(windows)
            done += 1
            if done % 500 == 0:
                print(f"  {done:,}/{len(sample):,}")

    elapsed = time.time() - start
    print(f"Done: {elapsed:.1f}s")

    # Save window-level data
    out_path = PROC_DIR / "phase0_3_window_sample.csv"
    with open(out_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=[
            "user_id", "window", "n_episodes", "n_adaptive", "n_questions",
            "n_correct", "R_b", "P", "gap"
        ])
        writer.writeheader()
        writer.writerows(all_windows)
    print(f"Saved: {out_path}")

    # Analysis
    students_with_data = set(w["user_id"] for w in all_windows)
    print(f"\nStudents with valid windows: {len(students_with_data):,}")

    r_b_values = [w["R_b"] for w in all_windows]
    p_values = [w["P"] for w in all_windows]
    gap_values = [w["gap"] for w in all_windows]

    print(f"\n{'='*60}")
    print(f"PHASE 0-3: WINDOW-LEVEL DISTRIBUTION")
    print(f"{'='*60}")
    print(f"Total windows: {len(all_windows):,}")

    # R_b distribution
    print(f"\nR_b (Reliance) distribution:")
    print(f"  Mean:   {statistics.mean(r_b_values):.4f}")
    print(f"  Median: {statistics.median(r_b_values):.4f}")
    print(f"  Std:    {statistics.stdev(r_b_values):.4f}")
    print(f"  Min:    {min(r_b_values):.4f}")
    print(f"  Max:    {max(r_b_values):.4f}")

    # Zero-inflation
    n_zero_rb = sum(1 for v in r_b_values if v == 0)
    n_near_zero_rb = sum(1 for v in r_b_values if v < 0.01)
    n_gt_01 = sum(1 for v in r_b_values if v >= 0.1)
    print(f"\n  R_b zero-inflation:")
    print(f"    R_b = 0:       {n_zero_rb:,} / {len(r_b_values):,} ({n_zero_rb/len(r_b_values)*100:.1f}%)")
    print(f"    R_b < 0.01:    {n_near_zero_rb:,} ({n_near_zero_rb/len(r_b_values)*100:.1f}%)")
    print(f"    R_b >= 0.10:   {n_gt_01:,} ({n_gt_01/len(r_b_values)*100:.1f}%)")

    # R_b by window position (does R_b change over time?)
    print(f"\n  R_b by window position (mean):")
    for w in range(1, N_WINDOWS + 1):
        vals = [x["R_b"] for x in all_windows if x["window"] == w]
        if vals:
            mean_rb = statistics.mean(vals)
            n_zero = sum(1 for v in vals if v == 0)
            print(f"    Window {w:>2}: R_b={mean_rb:.4f}, zero={n_zero/len(vals)*100:.0f}%")

    # P distribution
    print(f"\nP (Performance) distribution:")
    print(f"  Mean:   {statistics.mean(p_values):.4f}")
    print(f"  Median: {statistics.median(p_values):.4f}")
    print(f"  Std:    {statistics.stdev(p_values):.4f}")

    # Gap distribution
    print(f"\nCalibration Gap (R_b - P) distribution:")
    print(f"  Mean:   {statistics.mean(gap_values):.4f}")
    print(f"  Median: {statistics.median(gap_values):.4f}")
    print(f"  Std:    {statistics.stdev(gap_values):.4f}")

    # R_b × P correlation
    n = len(r_b_values)
    mean_rb = statistics.mean(r_b_values)
    mean_p = statistics.mean(p_values)
    cov = sum((r_b_values[i] - mean_rb) * (p_values[i] - mean_p) for i in range(n)) / (n - 1)
    std_rb = statistics.stdev(r_b_values)
    std_p = statistics.stdev(p_values)
    corr = cov / (std_rb * std_p) if std_rb > 0 and std_p > 0 else 0
    print(f"\nR_b × P correlation: r = {corr:.4f}")

    # Per-student: how many windows have R_b > 0?
    student_nonzero = defaultdict(int)
    student_total = defaultdict(int)
    for w in all_windows:
        student_total[w["user_id"]] += 1
        if w["R_b"] > 0:
            student_nonzero[w["user_id"]] += 1

    nonzero_counts = [student_nonzero.get(uid, 0) for uid in students_with_data]
    print(f"\nPer-student: windows with R_b > 0 (out of {N_WINDOWS}):")
    print(f"  Mean:   {statistics.mean(nonzero_counts):.1f}")
    print(f"  Median: {statistics.median(nonzero_counts):.0f}")

    buckets = [(0, 0), (1, 5), (6, 10), (11, 15), (16, 20)]
    for lo, hi in buckets:
        count = sum(1 for c in nonzero_counts if lo <= c <= hi)
        print(f"    {lo:>2}-{hi:>2} windows: {count:>5,} students ({count/len(nonzero_counts)*100:.1f}%)")


if __name__ == "__main__":
    main()
