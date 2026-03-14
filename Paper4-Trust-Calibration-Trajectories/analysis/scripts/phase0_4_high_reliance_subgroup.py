"""
Phase 0-4: High-reliance subgroup analysis.

The full sample has R_b ≈ 0 most of the time. Check if students with
higher adaptive_offer ratios show meaningful R_b variance for PP-GMM.

Also checks alternative window sizes (10, 5 instead of 20).
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


def parse_episodes(user_id: str) -> list:
    """Parse all episodes for a student."""
    filepath = RAW_DIR / f"{user_id}.csv"
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

            if action == "enter" and item_id.startswith("b"):
                if current is not None:
                    episodes.append(current)
                current = {
                    "timestamp": ts,
                    "source": src,
                    "is_adaptive": src == "adaptive_offer",
                    "correct": 0,
                    "total_q": 0,
                }
            elif action == "respond" and current is not None:
                q_id = item_id
                correct_ans = CORRECT_ANSWERS.get(q_id, "")
                is_correct = answer == correct_ans if correct_ans else False
                current["total_q"] += 1
                if is_correct:
                    current["correct"] += 1

    if current is not None:
        episodes.append(current)
    return episodes


def compute_multi_window(user_id: str) -> dict:
    """Compute R_b and P at multiple window sizes."""
    episodes = parse_episodes(user_id)
    n = len(episodes)
    if n < 20:
        return None

    result = {"user_id": user_id, "n_episodes": n}

    for n_win in [5, 10, 20]:
        win_size = n // n_win
        if win_size < 1:
            continue

        windows = []
        for w in range(n_win):
            start = w * win_size
            end = start + win_size if w < n_win - 1 else n
            eps = episodes[start:end]

            n_eps = len(eps)
            n_adp = sum(1 for e in eps if e["is_adaptive"])
            total_q = sum(e["total_q"] for e in eps)
            total_c = sum(e["correct"] for e in eps)

            r_b = n_adp / n_eps if n_eps > 0 else 0
            p = total_c / total_q if total_q > 0 else 0

            windows.append({"R_b": r_b, "P": p})

        # Store per-window stats
        rb_vals = [w["R_b"] for w in windows]
        p_vals = [w["P"] for w in windows]

        n_nonzero = sum(1 for v in rb_vals if v > 0)
        rb_mean = statistics.mean(rb_vals) if rb_vals else 0
        rb_std = statistics.stdev(rb_vals) if len(rb_vals) > 1 else 0
        p_mean = statistics.mean(p_vals) if p_vals else 0

        result[f"w{n_win}_rb_mean"] = rb_mean
        result[f"w{n_win}_rb_std"] = rb_std
        result[f"w{n_win}_rb_nonzero"] = n_nonzero
        result[f"w{n_win}_p_mean"] = p_mean
        result[f"w{n_win}_n_zero"] = n_win - n_nonzero

    return result


def main():
    global CORRECT_ANSWERS
    print("Loading correct answers...")
    CORRECT_ANSWERS = load_correct_answers()

    # Load all GMM-ready students with their adaptive ratios
    depth_path = PROC_DIR / "phase0_2_episode_depth.csv"
    students = []
    with open(depth_path, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if (int(row["total_episodes"]) >= 60
                and int(row["adaptive_episodes"]) >= 5
                and float(row["time_span_days"]) >= 1):
                students.append({
                    "user_id": row["user_id"],
                    "adaptive_ratio": float(row["adaptive_ratio"]),
                    "adaptive_episodes": int(row["adaptive_episodes"]),
                    "total_episodes": int(row["total_episodes"]),
                })

    print(f"GMM-ready: {len(students):,}")

    # Subgroup analysis by adaptive_offer ratio
    ratio_thresholds = [0.05, 0.10, 0.15, 0.20, 0.30]
    print(f"\n{'='*60}")
    print(f"SUBGROUP SIZES BY ADAPTIVE RATIO THRESHOLD")
    print(f"{'='*60}")
    for thresh in ratio_thresholds:
        n = sum(1 for s in students if s["adaptive_ratio"] >= thresh)
        median_eps = statistics.median([s["adaptive_episodes"] for s in students if s["adaptive_ratio"] >= thresh]) if n > 0 else 0
        median_total = statistics.median([s["total_episodes"] for s in students if s["adaptive_ratio"] >= thresh]) if n > 0 else 0
        print(f"  ratio ≥ {thresh:.2f}: {n:>6,} students | adaptive eps median: {median_eps:.0f} | total eps median: {median_total:.0f}")

    # Deep analysis on subgroups: ratio ≥ 0.10 and ratio ≥ 0.20
    for ratio_thresh in [0.10, 0.20]:
        subgroup = [s for s in students if s["adaptive_ratio"] >= ratio_thresh]
        if len(subgroup) < 100:
            print(f"\nSubgroup ratio ≥ {ratio_thresh}: too small ({len(subgroup)}), skipping")
            continue

        sample_size = min(1000, len(subgroup))
        random.seed(42)
        sample = random.sample(subgroup, sample_size)
        sample_ids = [s["user_id"] for s in sample]

        print(f"\n{'='*60}")
        print(f"SUBGROUP: adaptive_ratio ≥ {ratio_thresh} (N={len(subgroup):,}, sample={sample_size})")
        print(f"{'='*60}")

        results = []
        with ProcessPoolExecutor(max_workers=8, initializer=_init_worker, initargs=(CORRECT_ANSWERS,)) as executor:
            futures = {executor.submit(compute_multi_window, uid): uid for uid in sample_ids}
            for future in as_completed(futures):
                r = future.result()
                if r:
                    results.append(r)

        print(f"  Valid results: {len(results)}")

        for n_win in [5, 10, 20]:
            rb_means = [r[f"w{n_win}_rb_mean"] for r in results if f"w{n_win}_rb_mean" in r]
            rb_stds = [r[f"w{n_win}_rb_std"] for r in results if f"w{n_win}_rb_std" in r]
            n_zeros = [r[f"w{n_win}_n_zero"] for r in results if f"w{n_win}_n_zero" in r]
            rb_nonzeros = [r[f"w{n_win}_rb_nonzero"] for r in results if f"w{n_win}_rb_nonzero" in r]

            if not rb_means:
                continue

            pct_zero_windows = statistics.mean(n_zeros) / n_win * 100

            print(f"\n  {n_win} windows:")
            print(f"    R_b mean across students:        {statistics.mean(rb_means):.4f}")
            print(f"    R_b within-student std (mean):    {statistics.mean(rb_stds):.4f}")
            print(f"    Avg zero-windows per student:     {statistics.mean(n_zeros):.1f}/{n_win} ({pct_zero_windows:.0f}%)")
            print(f"    Students with ALL windows > 0:    {sum(1 for z in n_zeros if z == 0):,}/{len(n_zeros):,}")
            print(f"    Students with ≥50% windows > 0:   {sum(1 for nz in rb_nonzeros if nz >= n_win/2):,}/{len(rb_nonzeros):,}")

    # Finally: check students with ≥20 adaptive episodes AND ratio ≥ 0.10
    strict = [s for s in students if s["adaptive_ratio"] >= 0.10 and s["adaptive_episodes"] >= 20]
    print(f"\n{'='*60}")
    print(f"STRICT SUBGROUP: ratio ≥ 0.10 AND ≥20 adaptive episodes")
    print(f"{'='*60}")
    print(f"  N = {len(strict):,}")
    if strict:
        print(f"  Adaptive eps: median={statistics.median([s['adaptive_episodes'] for s in strict]):.0f}, "
              f"mean={statistics.mean([s['adaptive_episodes'] for s in strict]):.1f}")
        print(f"  Total eps: median={statistics.median([s['total_episodes'] for s in strict]):.0f}")
        print(f"  Ratio: median={statistics.median([s['adaptive_ratio'] for s in strict]):.3f}")

        sample_strict = random.sample(strict, min(500, len(strict)))
        results_strict = []
        with ProcessPoolExecutor(max_workers=8, initializer=_init_worker, initargs=(CORRECT_ANSWERS,)) as executor:
            futures = {executor.submit(compute_multi_window, uid): uid for uid in [s["user_id"] for s in sample_strict]}
            for future in as_completed(futures):
                r = future.result()
                if r:
                    results_strict.append(r)

        for n_win in [10, 20]:
            rb_stds = [r[f"w{n_win}_rb_std"] for r in results_strict if f"w{n_win}_rb_std" in r]
            n_zeros = [r[f"w{n_win}_n_zero"] for r in results_strict if f"w{n_win}_n_zero" in r]
            rb_nonzeros = [r[f"w{n_win}_rb_nonzero"] for r in results_strict if f"w{n_win}_rb_nonzero" in r]
            if rb_stds:
                print(f"\n  {n_win} windows:")
                print(f"    R_b within-student std: {statistics.mean(rb_stds):.4f}")
                print(f"    Avg zero-windows:       {statistics.mean(n_zeros):.1f}/{n_win}")
                print(f"    ≥50% non-zero windows:  {sum(1 for nz in rb_nonzeros if nz >= n_win/2):,}/{len(rb_nonzeros):,}")
                print(f"    ALL non-zero windows:   {sum(1 for z in n_zeros if z == 0):,}/{len(n_zeros):,}")


if __name__ == "__main__":
    main()
