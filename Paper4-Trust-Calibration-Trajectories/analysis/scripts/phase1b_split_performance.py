"""
Phase 1B: Re-operationalize with split performance metrics.

Extends Phase 1 by computing per-window:
  - P_adaptive:     accuracy on adaptive_offer problems only
  - P_non_adaptive: accuracy on non-adaptive problems only
  - AI_benefit:     P_adaptive - P_non_adaptive
  - calibration_gap_new: R_b - P_adaptive (commensurable gap)
  - expl_rate_adaptive: explanation rate on adaptive episodes specifically

Also computes within-student trajectory features:
  - R_b slope, variability, reversals, max_drop
  - P_adaptive slope, variability
  - AI_benefit slope, variability

Outputs:
  - phase1b_timeseries_long.csv   (extended long format)
  - phase1b_student_features.csv  (per-student trajectory features)
  - phase1b_exploratory.txt       (exploratory analysis summary)
"""

import csv
import time
import statistics
import numpy as np
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
    """Parse episodes with split adaptive/non-adaptive performance."""
    filepath = RAW_DIR / f"{user_id}.csv"

    # --- Parse episodes (same as Phase 1) ---
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
                    "bundle_id": item_id,
                    "correct": 0,
                    "total_q": 0,
                    "read_explanation": False,
                    "explanation_duration_ms": 0,
                    "answer_changes": 0,
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

    if current is not None:
        episodes.append(current)

    # Clean up
    for ep in episodes:
        ep.pop("responded_questions", None)
        ep.pop("_expl_enter_ts", None)

    n_episodes = len(episodes)
    if n_episodes < N_WINDOWS:
        return None

    # --- Compute windows with SPLIT performance ---
    window_size = n_episodes // N_WINDOWS
    windows = []

    for w in range(N_WINDOWS):
        start = w * window_size
        end = start + window_size if w < N_WINDOWS - 1 else n_episodes
        win_eps = episodes[start:end]

        n_eps = len(win_eps)
        adaptive_eps = [e for e in win_eps if e["is_adaptive"]]
        non_adaptive_eps = [e for e in win_eps if not e["is_adaptive"]]

        # Overall metrics
        n_adaptive = len(adaptive_eps)
        total_q = sum(e["total_q"] for e in win_eps)
        total_correct = sum(e["correct"] for e in win_eps)

        # Split performance
        adaptive_q = sum(e["total_q"] for e in adaptive_eps)
        adaptive_correct = sum(e["correct"] for e in adaptive_eps)
        non_adaptive_q = sum(e["total_q"] for e in non_adaptive_eps)
        non_adaptive_correct = sum(e["correct"] for e in non_adaptive_eps)

        # Explanation on adaptive specifically
        adaptive_expl = sum(1 for e in adaptive_eps if e["read_explanation"])
        adaptive_expl_dur = sum(e["explanation_duration_ms"] for e in adaptive_eps if e["read_explanation"])

        r_b = n_adaptive / n_eps if n_eps > 0 else 0.0
        p = total_correct / total_q if total_q > 0 else None
        p_adaptive = adaptive_correct / adaptive_q if adaptive_q > 0 else None
        p_non_adaptive = non_adaptive_correct / non_adaptive_q if non_adaptive_q > 0 else None

        # AI benefit: only when both are available
        ai_benefit = None
        if p_adaptive is not None and p_non_adaptive is not None:
            ai_benefit = p_adaptive - p_non_adaptive

        # New calibration gap (commensurable): R_b - P_adaptive
        # Both relate to adaptive content
        calibration_gap_new = None
        if p_adaptive is not None:
            calibration_gap_new = r_b - p_adaptive

        # Explanation rate on adaptive
        expl_rate_adaptive = adaptive_expl / n_adaptive if n_adaptive > 0 else None
        avg_expl_dur_adaptive = (adaptive_expl_dur / adaptive_expl / 1000) if adaptive_expl > 0 else 0.0

        # Overall explanation rate
        n_explanation = sum(1 for e in win_eps if e["read_explanation"])
        expl_rate = n_explanation / n_eps if n_eps > 0 else 0.0
        n_answer_change = sum(e["answer_changes"] for e in win_eps)
        change_rate = n_answer_change / n_eps if n_eps > 0 else 0.0

        windows.append({
            "user_id": user_id,
            "window": w + 1,
            "n_episodes": n_eps,
            "n_adaptive": n_adaptive,
            "n_non_adaptive": len(non_adaptive_eps),
            "n_questions": total_q,
            "n_adaptive_q": adaptive_q,
            "n_non_adaptive_q": non_adaptive_q,
            # Original metrics
            "R_b": round(r_b, 6),
            "P": round(p, 6) if p is not None else "",
            "gap": round(r_b - p, 6) if p is not None else "",
            # NEW split metrics
            "P_adaptive": round(p_adaptive, 6) if p_adaptive is not None else "",
            "P_non_adaptive": round(p_non_adaptive, 6) if p_non_adaptive is not None else "",
            "AI_benefit": round(ai_benefit, 6) if ai_benefit is not None else "",
            "calibration_gap_new": round(calibration_gap_new, 6) if calibration_gap_new is not None else "",
            # Explanation on adaptive
            "expl_rate_adaptive": round(expl_rate_adaptive, 6) if expl_rate_adaptive is not None else "",
            "avg_expl_dur_adaptive_s": round(avg_expl_dur_adaptive, 2),
            # Original auxiliary
            "expl_rate": round(expl_rate, 6),
            "answer_change_rate": round(change_rate, 6),
        })

    # --- Compute within-student trajectory features ---
    rb_series = [w["R_b"] for w in windows]
    p_adap_series = [w["P_adaptive"] for w in windows if w["P_adaptive"] != ""]
    ai_ben_series = [w["AI_benefit"] for w in windows if w["AI_benefit"] != ""]
    cal_gap_series = [w["calibration_gap_new"] for w in windows if w["calibration_gap_new"] != ""]

    def compute_trajectory_features(series, prefix):
        """Compute slope, variability, reversals, max_drop for a series."""
        if len(series) < 3:
            return {
                f"{prefix}_slope": "",
                f"{prefix}_sd": "",
                f"{prefix}_reversals": "",
                f"{prefix}_max_drop": "",
                f"{prefix}_range": "",
                f"{prefix}_mean": "",
            }

        # Convert to float
        vals = [float(v) for v in series]

        # Linear slope (simple: last - first normalized by length)
        slope = (vals[-1] - vals[0]) / (len(vals) - 1)

        # SD
        sd = statistics.stdev(vals) if len(vals) > 1 else 0.0

        # Direction reversals
        reversals = 0
        for i in range(2, len(vals)):
            d1 = vals[i - 1] - vals[i - 2]
            d2 = vals[i] - vals[i - 1]
            if (d1 > 0.001 and d2 < -0.001) or (d1 < -0.001 and d2 > 0.001):
                reversals += 1

        # Max drop
        max_drop = 0.0
        for i in range(1, len(vals)):
            drop = vals[i - 1] - vals[i]
            if drop > max_drop:
                max_drop = drop

        return {
            f"{prefix}_slope": round(slope, 6),
            f"{prefix}_sd": round(sd, 6),
            f"{prefix}_reversals": reversals,
            f"{prefix}_max_drop": round(max_drop, 6),
            f"{prefix}_range": round(max(vals) - min(vals), 6),
            f"{prefix}_mean": round(statistics.mean(vals), 6),
        }

    features = {"user_id": user_id}
    features.update(compute_trajectory_features(rb_series, "R_b"))
    features.update(compute_trajectory_features(
        [float(v) for v in p_adap_series], "P_adaptive"))
    features.update(compute_trajectory_features(
        [float(v) for v in ai_ben_series], "AI_benefit"))
    features.update(compute_trajectory_features(
        [float(v) for v in cal_gap_series], "cal_gap"))

    # Number of valid windows with both metrics
    features["n_valid_windows"] = len(ai_ben_series)

    return {"windows": windows, "features": features}


def main():
    global CORRECT_ANSWERS
    print("=" * 60)
    print("PHASE 1B: Split Performance Re-operationalization")
    print("=" * 60)

    print("\nLoading correct answers...")
    CORRECT_ANSWERS = load_correct_answers()
    print(f"  {len(CORRECT_ANSWERS):,} questions loaded")

    # Load target students
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

    print(f"Target students (ratio >= {ADAPTIVE_RATIO_THRESHOLD}): {len(target_students):,}")

    # Process
    all_windows = []
    all_features = []
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
                all_features.append(result["features"])
            done += 1
            if done % 1000 == 0:
                elapsed = time.time() - start
                rate = done / elapsed
                eta = (len(target_students) - done) / rate if rate > 0 else 0
                print(f"  {done:,}/{len(target_students):,} - {rate:.0f}/s - ETA {eta:.0f}s")

    elapsed = time.time() - start
    print(f"\nProcessed: {len(all_features):,} students ({skipped} skipped) in {elapsed:.1f}s")

    # Sort
    all_windows.sort(key=lambda x: (x["user_id"], x["window"]))
    all_features.sort(key=lambda x: x["user_id"])

    OUT_DIR.mkdir(parents=True, exist_ok=True)

    # Save extended time series
    ts_path = OUT_DIR / "phase1b_timeseries_long.csv"
    ts_fields = [
        "user_id", "window", "n_episodes", "n_adaptive", "n_non_adaptive",
        "n_questions", "n_adaptive_q", "n_non_adaptive_q",
        "R_b", "P", "gap",
        "P_adaptive", "P_non_adaptive", "AI_benefit", "calibration_gap_new",
        "expl_rate_adaptive", "avg_expl_dur_adaptive_s",
        "expl_rate", "answer_change_rate",
    ]
    with open(ts_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=ts_fields)
        writer.writeheader()
        writer.writerows(all_windows)
    print(f"\nSaved: {ts_path} ({len(all_windows):,} rows)")

    # Save student trajectory features
    feat_path = OUT_DIR / "phase1b_student_features.csv"
    feat_fields = [
        "user_id", "n_valid_windows",
        "R_b_slope", "R_b_sd", "R_b_reversals", "R_b_max_drop", "R_b_range", "R_b_mean",
        "P_adaptive_slope", "P_adaptive_sd", "P_adaptive_reversals", "P_adaptive_max_drop",
        "P_adaptive_range", "P_adaptive_mean",
        "AI_benefit_slope", "AI_benefit_sd", "AI_benefit_reversals", "AI_benefit_max_drop",
        "AI_benefit_range", "AI_benefit_mean",
        "cal_gap_slope", "cal_gap_sd", "cal_gap_reversals", "cal_gap_max_drop",
        "cal_gap_range", "cal_gap_mean",
    ]
    with open(feat_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=feat_fields)
        writer.writeheader()
        writer.writerows(all_features)
    print(f"Saved: {feat_path} ({len(all_features):,} rows)")

    # =========================================================
    # EXPLORATORY ANALYSIS
    # =========================================================
    print(f"\n{'=' * 60}")
    print("EXPLORATORY ANALYSIS")
    print(f"{'=' * 60}")

    report_lines = []
    def log(msg=""):
        print(msg)
        report_lines.append(msg)

    log("=" * 60)
    log("Phase 1B: Split Performance Exploratory Analysis")
    log("=" * 60)

    # --- Per-window split performance ---
    log("\n1. Per-Window Split Performance (Mean ± SD)")
    log(f"{'Window':>6} {'R_b':>8} {'P_all':>8} {'P_adap':>8} {'P_non':>8} "
        f"{'AI_ben':>8} {'Gap_old':>8} {'Gap_new':>8} {'N_adap':>8}")

    for w in range(1, N_WINDOWS + 1):
        w_data = [x for x in all_windows if x["window"] == w]
        n = len(w_data)

        rb = [x["R_b"] for x in w_data]
        p_all = [float(x["P"]) for x in w_data if x["P"] != ""]
        p_ad = [float(x["P_adaptive"]) for x in w_data if x["P_adaptive"] != ""]
        p_na = [float(x["P_non_adaptive"]) for x in w_data if x["P_non_adaptive"] != ""]
        ai_b = [float(x["AI_benefit"]) for x in w_data if x["AI_benefit"] != ""]
        g_old = [float(x["gap"]) for x in w_data if x["gap"] != ""]
        g_new = [float(x["calibration_gap_new"]) for x in w_data if x["calibration_gap_new"] != ""]
        n_ad_q = [x["n_adaptive_q"] for x in w_data]

        def fmt(vals):
            if not vals:
                return "    N/A"
            return f"{statistics.mean(vals):>+7.3f}"

        log(f"{w:>6} {fmt(rb)} {fmt(p_all)} {fmt(p_ad)} {fmt(p_na)} "
            f"{fmt(ai_b)} {fmt(g_old)} {fmt(g_new)} {statistics.mean(n_ad_q):>7.1f}")

    # --- P_adaptive distribution ---
    log("\n2. P_adaptive Distribution")
    all_p_ad = [float(x["P_adaptive"]) for x in all_windows if x["P_adaptive"] != ""]
    all_p_na = [float(x["P_non_adaptive"]) for x in all_windows if x["P_non_adaptive"] != ""]
    all_ai_b = [float(x["AI_benefit"]) for x in all_windows if x["AI_benefit"] != ""]

    if all_p_ad:
        log(f"  P_adaptive:     N={len(all_p_ad):,}, Mean={statistics.mean(all_p_ad):.4f}, "
            f"SD={statistics.stdev(all_p_ad):.4f}, "
            f"Median={statistics.median(all_p_ad):.4f}")
    if all_p_na:
        log(f"  P_non_adaptive: N={len(all_p_na):,}, Mean={statistics.mean(all_p_na):.4f}, "
            f"SD={statistics.stdev(all_p_na):.4f}, "
            f"Median={statistics.median(all_p_na):.4f}")
    if all_ai_b:
        log(f"  AI_benefit:     N={len(all_ai_b):,}, Mean={statistics.mean(all_ai_b):.4f}, "
            f"SD={statistics.stdev(all_ai_b):.4f}, "
            f"Median={statistics.median(all_ai_b):.4f}")
        n_pos = sum(1 for v in all_ai_b if v > 0)
        n_neg = sum(1 for v in all_ai_b if v < 0)
        n_zero = sum(1 for v in all_ai_b if v == 0)
        log(f"  AI_benefit > 0: {n_pos:,} ({n_pos/len(all_ai_b)*100:.1f}%) — AI helps")
        log(f"  AI_benefit < 0: {n_neg:,} ({n_neg/len(all_ai_b)*100:.1f}%) — AI hurts")
        log(f"  AI_benefit = 0: {n_zero:,} ({n_zero/len(all_ai_b)*100:.1f}%)")

    # --- New calibration gap ---
    log("\n3. New Calibration Gap (R_b - P_adaptive)")
    all_g_new = [float(x["calibration_gap_new"]) for x in all_windows if x["calibration_gap_new"] != ""]
    all_g_old = [float(x["gap"]) for x in all_windows if x["gap"] != ""]
    if all_g_new:
        log(f"  New gap:  Mean={statistics.mean(all_g_new):.4f}, SD={statistics.stdev(all_g_new):.4f}, "
            f"Median={statistics.median(all_g_new):.4f}")
    if all_g_old:
        log(f"  Old gap:  Mean={statistics.mean(all_g_old):.4f}, SD={statistics.stdev(all_g_old):.4f}, "
            f"Median={statistics.median(all_g_old):.4f}")
    if all_g_new:
        n_pos = sum(1 for v in all_g_new if v > 0)
        n_neg = sum(1 for v in all_g_new if v < 0)
        log(f"  Gap > 0 (over-reliance):  {n_pos:,} ({n_pos/len(all_g_new)*100:.1f}%)")
        log(f"  Gap < 0 (under-reliance): {n_neg:,} ({n_neg/len(all_g_new)*100:.1f}%)")
        log(f"  Gap range: [{min(all_g_new):.4f}, {max(all_g_new):.4f}]")

    # --- Windows with no adaptive questions ---
    log("\n4. Missing Data (windows with no adaptive questions)")
    n_missing_p_ad = sum(1 for x in all_windows if x["P_adaptive"] == "")
    n_missing_ai_b = sum(1 for x in all_windows if x["AI_benefit"] == "")
    log(f"  Windows missing P_adaptive: {n_missing_p_ad:,}/{len(all_windows):,} "
        f"({n_missing_p_ad/len(all_windows)*100:.1f}%)")
    log(f"  Windows missing AI_benefit: {n_missing_ai_b:,}/{len(all_windows):,} "
        f"({n_missing_ai_b/len(all_windows)*100:.1f}%)")

    # --- Trajectory features summary ---
    log("\n5. Within-Student Trajectory Features")

    def summarize_feature(name, feature_list):
        vals = [float(f[name]) for f in feature_list if f[name] != ""]
        if not vals:
            log(f"  {name}: N/A")
            return
        log(f"  {name}: N={len(vals):,}, Mean={statistics.mean(vals):.4f}, "
            f"SD={statistics.stdev(vals):.4f}, "
            f"Med={statistics.median(vals):.4f}, "
            f"[{min(vals):.4f}, {max(vals):.4f}]")

    log("\n  --- R_b trajectory features ---")
    summarize_feature("R_b_slope", all_features)
    summarize_feature("R_b_sd", all_features)
    summarize_feature("R_b_reversals", all_features)
    summarize_feature("R_b_max_drop", all_features)

    log("\n  --- P_adaptive trajectory features ---")
    summarize_feature("P_adaptive_slope", all_features)
    summarize_feature("P_adaptive_sd", all_features)
    summarize_feature("P_adaptive_reversals", all_features)
    summarize_feature("P_adaptive_max_drop", all_features)

    log("\n  --- AI_benefit trajectory features ---")
    summarize_feature("AI_benefit_slope", all_features)
    summarize_feature("AI_benefit_sd", all_features)
    summarize_feature("AI_benefit_reversals", all_features)
    summarize_feature("AI_benefit_max_drop", all_features)

    log("\n  --- New calibration gap trajectory features ---")
    summarize_feature("cal_gap_slope", all_features)
    summarize_feature("cal_gap_sd", all_features)
    summarize_feature("cal_gap_reversals", all_features)
    summarize_feature("cal_gap_max_drop", all_features)

    # --- Oscillation / Catastrophic candidates ---
    log("\n6. Pattern Candidates")

    # Oscillating: high reversals + moderate SD
    rb_reversals = [(f["user_id"], int(f["R_b_reversals"]))
                    for f in all_features if f["R_b_reversals"] != ""]
    if rb_reversals:
        high_reversal = [uid for uid, r in rb_reversals if r >= 5]
        log(f"  R_b reversals >= 5 (oscillating candidates): {len(high_reversal):,} "
            f"({len(high_reversal)/len(rb_reversals)*100:.1f}%)")

    p_ad_reversals = [(f["user_id"], int(f["P_adaptive_reversals"]))
                      for f in all_features if f["P_adaptive_reversals"] != ""]
    if p_ad_reversals:
        high_pa_rev = [uid for uid, r in p_ad_reversals if r >= 5]
        log(f"  P_adaptive reversals >= 5: {len(high_pa_rev):,} "
            f"({len(high_pa_rev)/len(p_ad_reversals)*100:.1f}%)")

    ai_b_reversals = [(f["user_id"], int(f["AI_benefit_reversals"]))
                      for f in all_features if f["AI_benefit_reversals"] != ""]
    if ai_b_reversals:
        high_ab_rev = [uid for uid, r in ai_b_reversals if r >= 5]
        log(f"  AI_benefit reversals >= 5: {len(high_ab_rev):,} "
            f"({len(high_ab_rev)/len(ai_b_reversals)*100:.1f}%)")

    cal_reversals = [(f["user_id"], int(f["cal_gap_reversals"]))
                     for f in all_features if f["cal_gap_reversals"] != ""]
    if cal_reversals:
        high_cal_rev = [uid for uid, r in cal_reversals if r >= 5]
        log(f"  Calibration gap reversals >= 5: {len(high_cal_rev):,} "
            f"({len(high_cal_rev)/len(cal_reversals)*100:.1f}%)")

    # Catastrophic: large max_drop in calibration gap
    cal_drops = [(f["user_id"], float(f["cal_gap_max_drop"]))
                 for f in all_features if f["cal_gap_max_drop"] != ""]
    if cal_drops:
        big_drops = [uid for uid, d in cal_drops if d > 0.20]
        log(f"  Calibration gap max_drop > 0.20 (catastrophic candidates): {len(big_drops):,} "
            f"({len(big_drops)/len(cal_drops)*100:.1f}%)")

    # Convergent: cal_gap slope toward 0 + decreasing SD
    cal_slopes = [(f["user_id"], float(f["cal_gap_slope"]))
                  for f in all_features if f["cal_gap_slope"] != ""]
    if cal_slopes:
        converging = [uid for uid, s in cal_slopes if s > 0.005]  # gap becoming less negative
        diverging = [uid for uid, s in cal_slopes if s < -0.005]
        flat = [uid for uid, s in cal_slopes if abs(s) <= 0.005]
        log(f"\n  Calibration gap slope distribution:")
        log(f"    Converging (slope > +0.005): {len(converging):,} "
            f"({len(converging)/len(cal_slopes)*100:.1f}%)")
        log(f"    Stagnant (|slope| <= 0.005): {len(flat):,} "
            f"({len(flat)/len(cal_slopes)*100:.1f}%)")
        log(f"    Diverging (slope < -0.005):  {len(diverging):,} "
            f"({len(diverging)/len(cal_slopes)*100:.1f}%)")

    # --- Key question: Does P_adaptive vary non-monotonically? ---
    log("\n7. Non-Monotonicity of P_adaptive")
    pa_rev_counts = [int(f["P_adaptive_reversals"]) for f in all_features
                     if f["P_adaptive_reversals"] != ""]
    if pa_rev_counts:
        rev_dist = {}
        for r in pa_rev_counts:
            rev_dist[r] = rev_dist.get(r, 0) + 1
        log(f"  Distribution of P_adaptive reversals:")
        for k in sorted(rev_dist.keys()):
            pct = rev_dist[k] / len(pa_rev_counts) * 100
            log(f"    {k} reversals: {rev_dist[k]:,} students ({pct:.1f}%)")

    # --- Comparison: Old gap vs New gap variability ---
    log("\n8. Gap Variability Comparison (Old vs New)")
    old_gap_sds = []
    new_gap_sds = []
    for f in all_features:
        # Compute old gap SD for this student from the windows
        uid = f["user_id"]
        student_windows = [w for w in all_windows if w["user_id"] == uid]
        old_gaps = [float(w["gap"]) for w in student_windows if w["gap"] != ""]
        new_gaps = [float(w["calibration_gap_new"]) for w in student_windows if w["calibration_gap_new"] != ""]
        if len(old_gaps) > 1:
            old_gap_sds.append(statistics.stdev(old_gaps))
        if len(new_gaps) > 1:
            new_gap_sds.append(statistics.stdev(new_gaps))

    if old_gap_sds and new_gap_sds:
        log(f"  Old gap (R_b - P) within-student SD: Mean={statistics.mean(old_gap_sds):.4f}, "
            f"Median={statistics.median(old_gap_sds):.4f}")
        log(f"  New gap (R_b - P_adaptive) within-student SD: Mean={statistics.mean(new_gap_sds):.4f}, "
            f"Median={statistics.median(new_gap_sds):.4f}")
        log(f"  Ratio (new/old): {statistics.mean(new_gap_sds)/statistics.mean(old_gap_sds):.2f}")

    # Save report
    report_path = OUT_DIR / "phase1b_exploratory.txt"
    with open(report_path, "w") as f:
        f.write("\n".join(report_lines))
    print(f"\nSaved: {report_path}")


if __name__ == "__main__":
    main()
