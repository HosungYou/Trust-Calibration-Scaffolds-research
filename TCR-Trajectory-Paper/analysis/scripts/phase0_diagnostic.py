"""
Phase 0: Data Diagnostic for Paper 4
Scans all EdNet KT3 files to identify adaptive_offer students and compute key statistics.

Output: data/ednet-kt3/processed/phase0_diagnostic.csv
"""

import os
import csv
import time
from pathlib import Path
from collections import Counter
from concurrent.futures import ProcessPoolExecutor, as_completed

RAW_DIR = Path("/Volumes/External SSD/Projects/Research/Trust-Calibration-Scaffolds-research/TCR-Trajectory-Paper/data/ednet-kt3/raw/KT3")
OUT_DIR = Path("/Volumes/External SSD/Projects/Research/Trust-Calibration-Scaffolds-research/TCR-Trajectory-Paper/data/ednet-kt3/processed")


def scan_student(filepath: Path) -> dict:
    """Scan a single student file for key diagnostics."""
    user_id = filepath.stem  # e.g., "u1"
    total_rows = 0
    n_adaptive = 0
    n_enter = 0
    source_counts = Counter()

    try:
        with open(filepath, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                total_rows += 1
                src = row.get("source", "")
                action = row.get("action_type", "")
                source_counts[src] += 1
                if src == "adaptive_offer":
                    n_adaptive += 1
                if action == "enter" and src == "adaptive_offer":
                    n_enter += 1
    except Exception as e:
        return {
            "user_id": user_id,
            "total_rows": 0,
            "n_adaptive_rows": 0,
            "n_adaptive_episodes": 0,
            "has_adaptive": False,
            "source_types": "",
            "error": str(e),
        }

    return {
        "user_id": user_id,
        "total_rows": total_rows,
        "n_adaptive_rows": n_adaptive,
        "n_adaptive_episodes": n_enter,  # enter actions = episode starts
        "has_adaptive": n_adaptive > 0,
        "source_types": ";".join(sorted(source_counts.keys())),
        "error": "",
    }


def main():
    files = sorted(RAW_DIR.glob("u*.csv"))
    total = len(files)
    print(f"Scanning {total:,} student files...")

    results = []
    start = time.time()

    # Process in parallel (8 workers)
    with ProcessPoolExecutor(max_workers=8) as executor:
        futures = {executor.submit(scan_student, f): f for f in files}
        done = 0
        for future in as_completed(futures):
            result = future.result()
            results.append(result)
            done += 1
            if done % 10000 == 0:
                elapsed = time.time() - start
                rate = done / elapsed
                eta = (total - done) / rate if rate > 0 else 0
                print(f"  {done:,}/{total:,} ({done/total*100:.1f}%) - {rate:.0f} files/s - ETA {eta:.0f}s")

    elapsed = time.time() - start
    print(f"\nScan complete: {total:,} files in {elapsed:.1f}s ({total/elapsed:.0f} files/s)")

    # Write full results
    out_path = OUT_DIR / "phase0_diagnostic.csv"
    results.sort(key=lambda x: x["user_id"])
    with open(out_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=[
            "user_id", "total_rows", "n_adaptive_rows", "n_adaptive_episodes",
            "has_adaptive", "source_types", "error"
        ])
        writer.writeheader()
        writer.writerows(results)
    print(f"Results saved: {out_path}")

    # Summary statistics
    n_with_adaptive = sum(1 for r in results if r["has_adaptive"])
    adaptive_students = [r for r in results if r["has_adaptive"]]
    episodes = [r["n_adaptive_episodes"] for r in adaptive_students]

    print(f"\n{'='*60}")
    print(f"PHASE 0 DIAGNOSTIC SUMMARY")
    print(f"{'='*60}")
    print(f"Total students:                {total:,}")
    print(f"Students with adaptive_offer:  {n_with_adaptive:,} ({n_with_adaptive/total*100:.1f}%)")
    print(f"Students without:              {total - n_with_adaptive:,} ({(total-n_with_adaptive)/total*100:.1f}%)")

    if episodes:
        import statistics
        print(f"\nAmong adaptive_offer students:")
        print(f"  Episodes min:    {min(episodes)}")
        print(f"  Episodes median: {statistics.median(episodes):.0f}")
        print(f"  Episodes mean:   {statistics.mean(episodes):.1f}")
        print(f"  Episodes max:    {max(episodes)}")
        print(f"  Episodes std:    {statistics.stdev(episodes):.1f}")

        # Distribution buckets
        buckets = [1, 5, 10, 20, 50, 100, 200, 500, 1000]
        print(f"\n  Episode count distribution:")
        prev = 0
        for b in buckets:
            count = sum(1 for e in episodes if prev < e <= b)
            if count > 0:
                print(f"    {prev+1:>4}-{b:>4}: {count:>6,} students ({count/len(episodes)*100:.1f}%)")
            prev = b
        count = sum(1 for e in episodes if e > buckets[-1])
        if count > 0:
            print(f"    {buckets[-1]+1:>4}+   : {count:>6,} students ({count/len(episodes)*100:.1f}%)")

    # Total rows distribution (all students)
    all_rows = [r["total_rows"] for r in results if r["total_rows"] > 0]
    if all_rows:
        import statistics
        print(f"\nAll students - total rows:")
        print(f"  Min:    {min(all_rows)}")
        print(f"  Median: {statistics.median(all_rows):.0f}")
        print(f"  Mean:   {statistics.mean(all_rows):.1f}")
        print(f"  Max:    {max(all_rows)}")

    # Source type prevalence
    all_sources = Counter()
    for r in results:
        for src in r["source_types"].split(";"):
            if src:
                all_sources[src] += 1
    print(f"\nSource type prevalence (# students with each source):")
    for src, count in all_sources.most_common():
        print(f"  {src:20s}: {count:>8,} ({count/total*100:.1f}%)")


if __name__ == "__main__":
    main()
