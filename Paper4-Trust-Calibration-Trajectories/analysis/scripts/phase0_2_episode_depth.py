"""
Phase 0-2: Episode depth analysis for adaptive_offer students.

For each student with adaptive_offer:
- Count total episodes (enter actions for bundles)
- Count adaptive_offer episodes specifically
- Compute time span
- Assess PP-GMM viability (need enough total episodes for 20 windows)

Input:  phase0_diagnostic.csv (student list)
Output: phase0_2_episode_depth.csv + summary
"""

import os
import csv
import time
import statistics
from pathlib import Path
from concurrent.futures import ProcessPoolExecutor, as_completed

RAW_DIR = Path("/Volumes/External SSD/Projects/Research/Trust-Calibration-Scaffolds-research/TCR-Trajectory-Paper/data/ednet-kt3/raw/KT3")
OUT_DIR = Path("/Volumes/External SSD/Projects/Research/Trust-Calibration-Scaffolds-research/TCR-Trajectory-Paper/data/ednet-kt3/processed")


def analyze_student(user_id: str) -> dict:
    """Parse episodes and compute depth statistics for one student."""
    filepath = RAW_DIR / f"{user_id}.csv"

    total_episodes = 0
    adaptive_episodes = 0
    source_episode_counts = {}
    timestamps = []
    respond_count = 0
    correct_count = 0  # we can't check this without metadata, skip for now

    try:
        with open(filepath, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                action = row.get("action_type", "")
                src = row.get("source", "")
                ts = int(row.get("timestamp", 0))

                if action == "enter" and row.get("item_id", "").startswith("b"):
                    # Bundle enter = episode start
                    total_episodes += 1
                    source_episode_counts[src] = source_episode_counts.get(src, 0) + 1
                    if src == "adaptive_offer":
                        adaptive_episodes += 1
                    timestamps.append(ts)

                if action == "respond":
                    respond_count += 1

    except Exception as e:
        return {"user_id": user_id, "error": str(e)}

    if not timestamps:
        return {
            "user_id": user_id,
            "total_episodes": 0,
            "adaptive_episodes": 0,
            "adaptive_ratio": 0,
            "time_span_hours": 0,
            "time_span_days": 0,
            "respond_count": 0,
            "episodes_per_source": "",
            "error": "",
        }

    time_span_ms = max(timestamps) - min(timestamps)
    time_span_hours = time_span_ms / (1000 * 3600)
    time_span_days = time_span_hours / 24

    return {
        "user_id": user_id,
        "total_episodes": total_episodes,
        "adaptive_episodes": adaptive_episodes,
        "adaptive_ratio": adaptive_episodes / total_episodes if total_episodes > 0 else 0,
        "time_span_hours": round(time_span_hours, 1),
        "time_span_days": round(time_span_days, 1),
        "respond_count": respond_count,
        "episodes_per_source": ";".join(f"{k}={v}" for k, v in sorted(source_episode_counts.items())),
        "error": "",
    }


def main():
    # Load adaptive_offer student list from Phase 0-1
    diag_path = OUT_DIR / "phase0_diagnostic.csv"
    adaptive_students = []
    with open(diag_path, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["has_adaptive"] == "True":
                adaptive_students.append(row["user_id"])

    total = len(adaptive_students)
    print(f"Analyzing episode depth for {total:,} adaptive_offer students...")

    results = []
    start = time.time()

    with ProcessPoolExecutor(max_workers=8) as executor:
        futures = {executor.submit(analyze_student, uid): uid for uid in adaptive_students}
        done = 0
        for future in as_completed(futures):
            result = future.result()
            results.append(result)
            done += 1
            if done % 5000 == 0:
                elapsed = time.time() - start
                rate = done / elapsed
                eta = (total - done) / rate if rate > 0 else 0
                print(f"  {done:,}/{total:,} ({done/total*100:.1f}%) - ETA {eta:.0f}s")

    elapsed = time.time() - start
    print(f"\nDone: {total:,} students in {elapsed:.1f}s")

    # Save results
    out_path = OUT_DIR / "phase0_2_episode_depth.csv"
    results.sort(key=lambda x: x["user_id"])
    fieldnames = [
        "user_id", "total_episodes", "adaptive_episodes", "adaptive_ratio",
        "time_span_hours", "time_span_days", "respond_count",
        "episodes_per_source", "error"
    ]
    with open(out_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)
    print(f"Saved: {out_path}")

    # Filter out errors
    valid = [r for r in results if not r.get("error") and r["total_episodes"] > 0]

    # Summary
    total_eps = [r["total_episodes"] for r in valid]
    adaptive_eps = [r["adaptive_episodes"] for r in valid]
    adaptive_ratios = [r["adaptive_ratio"] for r in valid]
    time_spans = [r["time_span_days"] for r in valid]

    print(f"\n{'='*60}")
    print(f"PHASE 0-2: EPISODE DEPTH SUMMARY")
    print(f"{'='*60}")
    print(f"Valid students: {len(valid):,}")

    print(f"\nTotal episodes per student:")
    print(f"  Min:    {min(total_eps)}")
    print(f"  Q1:     {statistics.quantiles(total_eps, n=4)[0]:.0f}")
    print(f"  Median: {statistics.median(total_eps):.0f}")
    print(f"  Q3:     {statistics.quantiles(total_eps, n=4)[2]:.0f}")
    print(f"  Mean:   {statistics.mean(total_eps):.1f}")
    print(f"  Max:    {max(total_eps)}")

    print(f"\nAdaptive_offer episodes per student:")
    print(f"  Min:    {min(adaptive_eps)}")
    print(f"  Median: {statistics.median(adaptive_eps):.0f}")
    print(f"  Mean:   {statistics.mean(adaptive_eps):.1f}")
    print(f"  Max:    {max(adaptive_eps)}")

    print(f"\nAdaptive_offer ratio (adaptive / total episodes):")
    print(f"  Min:    {min(adaptive_ratios):.3f}")
    print(f"  Median: {statistics.median(adaptive_ratios):.3f}")
    print(f"  Mean:   {statistics.mean(adaptive_ratios):.3f}")
    print(f"  Max:    {max(adaptive_ratios):.3f}")

    print(f"\nTime span (days):")
    print(f"  Min:    {min(time_spans):.1f}")
    print(f"  Median: {statistics.median(time_spans):.1f}")
    print(f"  Mean:   {statistics.mean(time_spans):.1f}")
    print(f"  Max:    {max(time_spans):.1f}")

    # GMM viability thresholds
    print(f"\n{'='*60}")
    print(f"PP-GMM VIABILITY (minimum total episodes for 20 windows)")
    print(f"{'='*60}")
    thresholds = [20, 40, 60, 80, 100, 150, 200]
    for t in thresholds:
        n = sum(1 for e in total_eps if e >= t)
        # Also check they have at least some adaptive episodes
        n_with_adaptive_min5 = sum(
            1 for r in valid if r["total_episodes"] >= t and r["adaptive_episodes"] >= 5
        )
        print(f"  ≥{t:>4} total eps: {n:>6,} students | with ≥5 adaptive eps: {n_with_adaptive_min5:>6,}")

    # Additional: filter for GMM-ready students (≥60 episodes, ≥5 adaptive, ≥1 day span)
    gmm_ready = [
        r for r in valid
        if r["total_episodes"] >= 60
        and r["adaptive_episodes"] >= 5
        and r["time_span_days"] >= 1
    ]
    print(f"\n  GMM-READY (≥60 eps, ≥5 adaptive, ≥1 day): {len(gmm_ready):,} students")

    if gmm_ready:
        gmm_total = [r["total_episodes"] for r in gmm_ready]
        gmm_adaptive = [r["adaptive_episodes"] for r in gmm_ready]
        gmm_ratio = [r["adaptive_ratio"] for r in gmm_ready]
        print(f"    Total episodes:    median={statistics.median(gmm_total):.0f}, mean={statistics.mean(gmm_total):.1f}")
        print(f"    Adaptive episodes: median={statistics.median(gmm_adaptive):.0f}, mean={statistics.mean(gmm_adaptive):.1f}")
        print(f"    Adaptive ratio:    median={statistics.median(gmm_ratio):.3f}, mean={statistics.mean(gmm_ratio):.3f}")
        print(f"    Time span (days):  median={statistics.median([r['time_span_days'] for r in gmm_ready]):.1f}")


if __name__ == "__main__":
    main()
