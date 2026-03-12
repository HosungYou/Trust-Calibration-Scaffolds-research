#!/usr/bin/env python3
"""
Chess Puzzle Trust Calibration Analysis Pipeline
=================================================
Bondi et al. (2023) data — Independent analysis for TCR research program

Data structure:
- 50 participants × 2 conditions = 100 files
- Condition 1 (_1): High→Low AI reliability (~80%→~20% at trial 20)
- Condition 2 (_2): Low→High AI reliability (~20%→~80% at trial 20)
- 30 experimental trials per session + 3 practice trials
- Per trial: bmove1 (initial), aisugg (AI), bmove2 (final after seeing AI),
             multiPV (AI suggestion rank, 1=best 7=worst), feedback1/2 (±5)

Key variables:
- followed_ai: bmove2 == aisugg (behavioral reliance decision)
- ai_accurate: multiPV == 1 (AI suggestion is objectively best move)
- trial_correct: feedback2 == +5 (final move was correct)
- cal_gap: R_b − AI_accuracy (positive = over-reliance, negative = under-reliance)

Windowing: 6 windows × 5 trials (switch at trial 20 = between W4 and W5)

Output:
- chess_trial_level.csv: Trial-level data (~3000 rows)
- chess_window_level.csv: Window-level aggregated data (~600 rows)
- chess_participant_features.csv: Per-session trajectory features (~100 rows)
- chess_exploratory.txt: Descriptive statistics and pattern analysis
"""

import os
import csv
import numpy as np
from collections import defaultdict

# =============================================================================
# Configuration
# =============================================================================
BASE_DIR = "/Volumes/External SSD/Projects/Research/Trust-Calibration-Scaffolds-research/Chess-Puzzle-Analysis"
DATA_DIR = os.path.join(BASE_DIR, "data", "Data")
OUTPUT_DIR = os.path.join(BASE_DIR, "analysis", "outputs")
WINDOW_SIZE = 5
N_TRIALS = 30
N_WINDOWS = N_TRIALS // WINDOW_SIZE  # 6

os.makedirs(OUTPUT_DIR, exist_ok=True)


# =============================================================================
# Data Parsing
# =============================================================================
def parse_chess_file(filepath):
    """
    Parse a single chess puzzle CSV file.

    File structure (0-indexed):
      Row 0: Header
      Row 1: Initial confidence values (selfconf, aiconf baseline)
      Rows 2-4: Practice trials (3)
      Row 5: Mid-point Score
      Rows 6-35: Experimental trials (30)
      Row 36: Final Score
    """
    with open(filepath, 'r') as f:
        reader = csv.reader(f)
        rows = list(reader)

    # Initial confidence
    initial_selfconf = _to_float(rows[1][8])
    initial_aiconf = _to_float(rows[1][9])

    # Extract 30 experimental trials (rows 6-35, 0-indexed)
    trials = []
    for i in range(6, 36):
        row = rows[i]
        if row[0] == 'Score':
            continue  # safety: skip stray Score rows

        trial_num = i - 5  # 1-based trial number (1–30)

        bmove1 = row[2].strip() if row[2] else ''
        aisugg = row[3].strip() if row[3] else ''
        multiPV = _to_int(row[4])
        bmove2 = row[5].strip() if row[5] else ''
        feedback1 = _to_int(row[6])
        feedback2 = _to_int(row[7])
        selfconf = _to_float(row[8])
        aiconf = _to_float(row[9])

        # Core behavioral variables
        followed_ai = 1 if bmove2 == aisugg else 0
        ai_accurate = 1 if multiPV == 1 else 0
        trial_correct = 1 if feedback2 == 5 else 0
        initial_correct = 1 if feedback1 == 5 else 0

        # Switch behavior
        switched_to_ai = 1 if (bmove1 != aisugg and bmove2 == aisugg) else 0
        switched_from_ai = 1 if (bmove1 == aisugg and bmove2 != aisugg) else 0
        stayed_with_own = 1 if (bmove1 != aisugg and bmove2 != aisugg) else 0
        stayed_with_ai = 1 if (bmove1 == aisugg and bmove2 == aisugg) else 0

        # Outcome of reliance decision
        if followed_ai:
            reliance_outcome = 'correct' if trial_correct else 'incorrect'
        else:
            reliance_outcome = 'correct' if trial_correct else 'incorrect'
        # More precise: did following AI help or hurt?
        ai_helped = (trial_correct == 1 and initial_correct == 0 and followed_ai == 1)
        ai_hurt = (trial_correct == 0 and initial_correct == 1 and followed_ai == 1)

        trials.append({
            'trial_num': trial_num,
            'bmove1': bmove1,
            'aisugg': aisugg,
            'bmove2': bmove2,
            'multiPV': multiPV,
            'feedback1': feedback1,
            'feedback2': feedback2,
            'selfconf': selfconf,
            'aiconf': aiconf,
            'followed_ai': followed_ai,
            'ai_accurate': ai_accurate,
            'trial_correct': trial_correct,
            'initial_correct': initial_correct,
            'switched_to_ai': switched_to_ai,
            'switched_from_ai': switched_from_ai,
            'stayed_with_own': stayed_with_own,
            'stayed_with_ai': stayed_with_ai,
            'ai_helped': 1 if ai_helped else 0,
            'ai_hurt': 1 if ai_hurt else 0,
        })

    return trials, initial_selfconf, initial_aiconf


def _to_float(val):
    try:
        return float(val) if val and val != 'None' else np.nan
    except ValueError:
        return np.nan


def _to_int(val):
    try:
        return int(val) if val and val != 'None' else np.nan
    except ValueError:
        return np.nan


# =============================================================================
# Window Aggregation
# =============================================================================
def compute_window_metrics(trials, window_size=5):
    """Aggregate trial-level data into windows."""
    windows = []
    n_windows = len(trials) // window_size

    for w in range(n_windows):
        wt = trials[w * window_size : (w + 1) * window_size]

        followed = [t['followed_ai'] for t in wt]
        ai_acc = [t['ai_accurate'] for t in wt]
        correct = [t['trial_correct'] for t in wt]
        init_correct = [t['initial_correct'] for t in wt]
        sc = [t['selfconf'] for t in wt if not np.isnan(t['selfconf'])]
        ac = [t['aiconf'] for t in wt if not np.isnan(t['aiconf'])]

        R_b = np.mean(followed)
        AI_accuracy = np.mean(ai_acc)
        P = np.mean(correct)
        P_initial = np.mean(init_correct)
        cal_gap = R_b - AI_accuracy

        # Appropriate reliance: follow accurate AI or ignore inaccurate AI
        n_appropriate = sum(
            1 for t in wt
            if (t['followed_ai'] and t['ai_accurate'])
            or (not t['followed_ai'] and not t['ai_accurate'])
        )
        appropriate_reliance = n_appropriate / len(wt)

        # Switch behavior
        switch_to_ai = np.mean([t['switched_to_ai'] for t in wt])
        switch_from_ai = np.mean([t['switched_from_ai'] for t in wt])

        # Performance improvement from AI
        perf_gain = P - P_initial  # positive = AI improved outcomes

        windows.append({
            'window': w + 1,
            'R_b': round(R_b, 4),
            'AI_accuracy': round(AI_accuracy, 4),
            'P': round(P, 4),
            'P_initial': round(P_initial, 4),
            'cal_gap': round(cal_gap, 4),
            'appropriate_reliance': round(appropriate_reliance, 4),
            'perf_gain': round(perf_gain, 4),
            'selfconf': round(np.mean(sc), 4) if sc else np.nan,
            'aiconf': round(np.mean(ac), 4) if ac else np.nan,
            'switch_to_ai': round(switch_to_ai, 4),
            'switch_from_ai': round(switch_from_ai, 4),
            'n_followed': sum(followed),
            'n_ai_accurate': sum(ai_acc),
            'n_correct': sum(correct),
        })

    return windows


# =============================================================================
# Trajectory Feature Extraction
# =============================================================================
def compute_trajectory_features(windows):
    """Extract within-session trajectory features for GMM input."""
    n = len(windows)
    if n < 3:
        return None

    features = {}

    for name in ['R_b', 'AI_accuracy', 'cal_gap', 'P', 'appropriate_reliance']:
        arr = np.array([w[name] for w in windows], dtype=float)
        x = np.arange(len(arr))

        # Linear slope
        slope = np.polyfit(x, arr, 1)[0] if len(arr) > 1 else 0.0

        # Variability
        sd = float(np.std(arr, ddof=1)) if len(arr) > 1 else 0.0
        mean_val = float(np.mean(arr))
        range_val = float(np.ptp(arr))

        # Reversals (non-monotonicity)
        diffs = np.diff(arr)
        signs = np.sign(diffs)
        signs_nz = signs[signs != 0]
        reversals = int(np.sum(np.abs(np.diff(signs_nz))) // 2) if len(signs_nz) > 1 else 0

        # Max drop / rise
        max_drop = float(abs(min(diffs))) if len(diffs) > 0 and min(diffs) < 0 else 0.0
        max_rise = float(max(diffs)) if len(diffs) > 0 and max(diffs) > 0 else 0.0

        # Pre-switch (W1-W4) vs post-switch (W5-W6)
        pre_mean = float(np.mean(arr[:4]))
        post_mean = float(np.mean(arr[4:])) if len(arr) > 4 else float(np.mean(arr))
        switch_effect = post_mean - pre_mean

        # Window 4→5 jump (the switch point)
        switch_jump = float(arr[4] - arr[3]) if len(arr) > 4 else 0.0

        features[f'{name}_slope'] = round(slope, 6)
        features[f'{name}_sd'] = round(sd, 6)
        features[f'{name}_mean'] = round(mean_val, 6)
        features[f'{name}_range'] = round(range_val, 6)
        features[f'{name}_reversals'] = reversals
        features[f'{name}_max_drop'] = round(max_drop, 6)
        features[f'{name}_max_rise'] = round(max_rise, 6)
        features[f'{name}_pre_mean'] = round(pre_mean, 6)
        features[f'{name}_post_mean'] = round(post_mean, 6)
        features[f'{name}_switch_effect'] = round(switch_effect, 6)
        features[f'{name}_switch_jump'] = round(switch_jump, 6)

    # Wide-format window values (for direct GMM input)
    for w_obj in windows:
        w = w_obj['window']
        features[f'R_b_w{w}'] = w_obj['R_b']
        features[f'AI_acc_w{w}'] = w_obj['AI_accuracy']
        features[f'cal_gap_w{w}'] = w_obj['cal_gap']
        features[f'P_w{w}'] = w_obj['P']
        features[f'approp_w{w}'] = w_obj['appropriate_reliance']

    return features


# =============================================================================
# Main Pipeline
# =============================================================================
def main():
    print("=" * 70)
    print("CHESS PUZZLE TRUST CALIBRATION ANALYSIS PIPELINE")
    print("Bondi et al. (2023) — Independent Analysis")
    print("=" * 70)

    # ----- 1. Parse all files -----
    all_trials = []
    all_windows = []
    all_features = []
    parse_errors = []

    csv_files = sorted(f for f in os.listdir(DATA_DIR) if f.endswith('.csv'))
    print(f"\nFound {len(csv_files)} CSV files in {DATA_DIR}")

    for fname in csv_files:
        # Filename pattern: data{N}_{condition}.csv
        base = fname.replace('.csv', '').replace('data', '')
        parts = base.split('_')
        participant_id = int(parts[0])
        condition = int(parts[1])  # 1=High→Low, 2=Low→High
        condition_label = "High_to_Low" if condition == 1 else "Low_to_High"
        session_id = f"P{participant_id:02d}_C{condition}"

        filepath = os.path.join(DATA_DIR, fname)
        try:
            trials, init_sc, init_ac = parse_chess_file(filepath)
        except Exception as e:
            parse_errors.append(f"{fname}: {e}")
            continue

        if len(trials) != N_TRIALS:
            parse_errors.append(f"{fname}: got {len(trials)} trials (expected {N_TRIALS})")
            continue

        # Verify AI accuracy pattern
        pre_ai_acc = np.mean([t['ai_accurate'] for t in trials[:20]])
        post_ai_acc = np.mean([t['ai_accurate'] for t in trials[20:]])

        # Attach metadata
        for t in trials:
            t.update({
                'participant_id': participant_id,
                'condition': condition,
                'condition_label': condition_label,
                'session_id': session_id,
                'phase': 'pre_switch' if t['trial_num'] <= 20 else 'post_switch',
            })
            all_trials.append(t)

        # Windows
        windows = compute_window_metrics(trials, WINDOW_SIZE)
        for w in windows:
            w.update({
                'participant_id': participant_id,
                'condition': condition,
                'condition_label': condition_label,
                'session_id': session_id,
                'phase': 'pre_switch' if w['window'] <= 4 else 'post_switch',
            })
            all_windows.append(w)

        # Features
        feat = compute_trajectory_features(windows)
        if feat:
            feat.update({
                'participant_id': participant_id,
                'condition': condition,
                'condition_label': condition_label,
                'session_id': session_id,
                'initial_selfconf': init_sc,
                'initial_aiconf': init_ac,
                'pre_ai_accuracy': round(pre_ai_acc, 3),
                'post_ai_accuracy': round(post_ai_acc, 3),
            })
            all_features.append(feat)

    print(f"\nParsed successfully: {len(all_features)} sessions")
    print(f"  Condition 1 (High→Low): {sum(1 for f in all_features if f['condition'] == 1)}")
    print(f"  Condition 2 (Low→High): {sum(1 for f in all_features if f['condition'] == 2)}")
    if parse_errors:
        print(f"  Parse errors: {len(parse_errors)}")
        for e in parse_errors:
            print(f"    {e}")

    # ----- 2. Save trial-level data -----
    trial_cols = [
        'session_id', 'participant_id', 'condition', 'condition_label',
        'trial_num', 'phase',
        'followed_ai', 'ai_accurate', 'trial_correct', 'initial_correct',
        'switched_to_ai', 'switched_from_ai', 'stayed_with_own', 'stayed_with_ai',
        'ai_helped', 'ai_hurt',
        'selfconf', 'aiconf', 'multiPV', 'feedback1', 'feedback2',
    ]
    _save_csv(os.path.join(OUTPUT_DIR, 'chess_trial_level.csv'), all_trials, trial_cols)

    # ----- 3. Save window-level data -----
    window_cols = [
        'session_id', 'participant_id', 'condition', 'condition_label',
        'window', 'phase',
        'R_b', 'AI_accuracy', 'P', 'P_initial', 'cal_gap',
        'appropriate_reliance', 'perf_gain',
        'selfconf', 'aiconf',
        'switch_to_ai', 'switch_from_ai',
        'n_followed', 'n_ai_accurate', 'n_correct',
    ]
    _save_csv(os.path.join(OUTPUT_DIR, 'chess_window_level.csv'), all_windows, window_cols)

    # ----- 4. Save features -----
    if all_features:
        meta_cols = ['session_id', 'participant_id', 'condition', 'condition_label',
                     'initial_selfconf', 'initial_aiconf', 'pre_ai_accuracy', 'post_ai_accuracy']
        other_cols = sorted(k for k in all_features[0] if k not in meta_cols)
        _save_csv(os.path.join(OUTPUT_DIR, 'chess_participant_features.csv'),
                  all_features, meta_cols + other_cols)

    # ----- 5. Exploratory analysis -----
    report = _exploratory_analysis(all_trials, all_windows, all_features)
    report_path = os.path.join(OUTPUT_DIR, 'chess_exploratory.txt')
    with open(report_path, 'w') as f:
        f.write(report)
    print(f"\nSaved: {report_path}")
    print("\n" + report)


# =============================================================================
# Exploratory Analysis
# =============================================================================
def _exploratory_analysis(trials, windows, features):
    R = []
    R.append("=" * 70)
    R.append("CHESS PUZZLE TRUST CALIBRATION — EXPLORATORY ANALYSIS")
    R.append("Bondi et al. (2023)")
    R.append("=" * 70)

    n_c1 = sum(1 for f in features if f['condition'] == 1)
    n_c2 = sum(1 for f in features if f['condition'] == 2)

    # --- 1. Overall Summary ---
    R.append("\n## 1. OVERALL SUMMARY")
    R.append(f"Sessions: {len(features)} (C1 High→Low: {n_c1}, C2 Low→High: {n_c2})")
    R.append(f"Trials: {len(trials)}, Windows: {len(windows)}")
    R.append(f"Window size: {WINDOW_SIZE} trials, {N_WINDOWS} windows per session")
    R.append(f"Switch point: trial 20 (between window 4 and 5)")

    # --- 2. Trial-Level Summary ---
    R.append("\n## 2. TRIAL-LEVEL STATISTICS")
    R.append(f"Overall follow rate: {_m(trials, 'followed_ai'):.3f}")
    R.append(f"Overall AI accuracy: {_m(trials, 'ai_accurate'):.3f}")
    R.append(f"Overall correct rate: {_m(trials, 'trial_correct'):.3f}")

    R.append("\n### By Condition × Phase:")
    R.append(f"  {'Condition':<15} {'Phase':<15} {'Follow':>7} {'AI_acc':>7} {'Correct':>7} {'Approp':>7}")
    R.append(f"  {'-'*15} {'-'*15} {'-'*7} {'-'*7} {'-'*7} {'-'*7}")
    for c, cl in [(1, 'High→Low'), (2, 'Low→High')]:
        for ph in ['pre_switch', 'post_switch']:
            ct = [t for t in trials if t['condition'] == c and t['phase'] == ph]
            if not ct:
                continue
            fol = _m(ct, 'followed_ai')
            acc = _m(ct, 'ai_accurate')
            cor = _m(ct, 'trial_correct')
            # appropriate
            app = np.mean([
                1 if (t['followed_ai'] and t['ai_accurate']) or
                     (not t['followed_ai'] and not t['ai_accurate']) else 0
                for t in ct
            ])
            R.append(f"  {cl:<15} {ph:<15} {fol:>7.3f} {acc:>7.3f} {cor:>7.3f} {app:>7.3f}")

    # --- 3. Window Trajectories ---
    R.append("\n## 3. WINDOW-LEVEL TRAJECTORIES (Mean ± SD)")
    for c, cl in [(1, 'High→Low'), (2, 'Low→High')]:
        R.append(f"\n### Condition {c} ({cl}):")
        R.append(f"  {'W':>3}  {'R_b':>10}  {'AI_acc':>10}  {'P':>10}  {'Gap':>10}  {'Approp':>10}")
        R.append(f"  {'---':>3}  {'----------':>10}  {'----------':>10}  {'----------':>10}  {'----------':>10}  {'----------':>10}")
        for w in range(1, N_WINDOWS + 1):
            wd = [d for d in windows if d['condition'] == c and d['window'] == w]
            if not wd:
                continue
            def _ms(data, key):
                vals = [d[key] for d in data]
                return f"{np.mean(vals):.3f}±{np.std(vals):.2f}"
            switch_marker = " ◄" if w == 5 else ""
            R.append(f"  {w:>3}  {_ms(wd,'R_b'):>10}  {_ms(wd,'AI_accuracy'):>10}  "
                     f"{_ms(wd,'P'):>10}  {_ms(wd,'cal_gap'):>10}  "
                     f"{_ms(wd,'appropriate_reliance'):>10}{switch_marker}")

    # --- 4. Switch Effect ---
    R.append("\n## 4. RELIABILITY SWITCH EFFECT (Pre W1-W4 vs Post W5-W6)")
    for c, cl in [(1, 'High→Low'), (2, 'Low→High')]:
        cf = [f for f in features if f['condition'] == c]
        R.append(f"\n### Condition {c} ({cl}), N={len(cf)}:")
        for var in ['R_b', 'cal_gap', 'appropriate_reliance']:
            pre = np.array([f[f'{var}_pre_mean'] for f in cf])
            post = np.array([f[f'{var}_post_mean'] for f in cf])
            eff = np.array([f[f'{var}_switch_effect'] for f in cf])
            jump = np.array([f[f'{var}_switch_jump'] for f in cf])
            pool_sd = np.sqrt((np.std(pre)**2 + np.std(post)**2) / 2)
            d = np.mean(eff) / pool_sd if pool_sd > 0 else 0

            R.append(f"  {var}:")
            R.append(f"    Pre:  {np.mean(pre):.3f} ± {np.std(pre):.3f}")
            R.append(f"    Post: {np.mean(post):.3f} ± {np.std(post):.3f}")
            R.append(f"    Effect: {np.mean(eff):+.3f} (d={d:+.2f})")
            R.append(f"    W4→W5 jump: {np.mean(jump):+.3f} ± {np.std(jump):.3f}")

    # --- 5. Trajectory Feature Distributions ---
    R.append("\n## 5. TRAJECTORY FEATURES (Mean ± SD)")
    for c, cl in [(1, 'High→Low'), (2, 'Low→High')]:
        cf = [f for f in features if f['condition'] == c]
        R.append(f"\n### Condition {c} ({cl}):")
        for var in ['R_b', 'cal_gap']:
            slopes = [f[f'{var}_slope'] for f in cf]
            sds = [f[f'{var}_sd'] for f in cf]
            revs = [f[f'{var}_reversals'] for f in cf]
            drops = [f[f'{var}_max_drop'] for f in cf]
            R.append(f"  {var}:")
            R.append(f"    Slope:     {np.mean(slopes):+.4f} ± {np.std(slopes):.4f}")
            R.append(f"    SD:        {np.mean(sds):.4f} ± {np.std(sds):.4f}")
            R.append(f"    Reversals: {np.mean(revs):.2f} ± {np.std(revs):.2f}")
            R.append(f"    Max drop:  {np.mean(drops):.4f} ± {np.std(drops):.4f}")

    # --- 6. Rule-Based Pattern Classification ---
    R.append("\n## 6. PRELIMINARY PATTERN CLASSIFICATION (Rule-Based)")
    patterns = defaultdict(lambda: {'C1': 0, 'C2': 0})

    for f in features:
        ck = f'C{f["condition"]}'
        gs = f['cal_gap_slope']
        gsd = f['cal_gap_sd']
        grev = f['cal_gap_reversals']
        gswitch = f['cal_gap_switch_effect']
        gjump = f['cal_gap_switch_jump']

        # Convergent: gap magnitude decreasing over time
        if gs > 0.02 and gsd < 0.20:
            patterns['Convergent'][ck] += 1

        # Oscillating: high variability with reversals
        if grev >= 2 and gsd > 0.15:
            patterns['Oscillating'][ck] += 1

        # Stagnant: flat, low variability
        if abs(gs) < 0.01 and gsd < 0.10:
            patterns['Stagnant'][ck] += 1

        # Catastrophic: large sudden gap change at switch
        if abs(gjump) > 0.3:
            patterns['Catastrophic_jump'][ck] += 1

        # Over-reliance post-switch (C1: AI bad but still followed)
        if f['condition'] == 1:
            post_rb = f['R_b_post_mean']
            post_ai = f['AI_accuracy_post_mean']
            if post_rb > post_ai + 0.15:
                patterns['Over_reliance_post'][ck] += 1
            if post_rb > post_ai:
                patterns['Over_reliance_any'][ck] += 1

        # Under-reliance post-switch (C2: AI good but not followed)
        if f['condition'] == 2:
            post_rb = f['R_b_post_mean']
            post_ai = f['AI_accuracy_post_mean']
            if post_ai > post_rb + 0.3:
                patterns['Under_reliance_post'][ck] += 1

    R.append(f"\n  {'Pattern':<30}  {'C1':>5}  {'C2':>5}  {'Total':>5}")
    R.append(f"  {'-'*30}  {'-'*5}  {'-'*5}  {'-'*5}")
    for pat, counts in sorted(patterns.items()):
        tot = counts['C1'] + counts['C2']
        R.append(f"  {pat:<30}  {counts['C1']:>5}  {counts['C2']:>5}  {tot:>5}")

    # --- 7. Theory Mapping ---
    R.append("\n## 7. THEORETICAL PATTERN MAPPING")
    R.append("""
  CONDITION 1 (High→Low): AI reliability drops from ~80% to ~20% at trial 20
    Expected patterns:
    - Pre-switch (W1-W4): Participants learn AI is good → increase reliance → CONVERGENT
    - Post-switch (W5-W6): AI becomes bad but reliance may persist → OVER-RELIANCE
    - Over time if reliance drops: OSCILLATING → eventually CONVERGENT
    - If reliance stays high despite bad AI: CATASTROPHIC (over-reliance harm)

  CONDITION 2 (Low→High): AI reliability rises from ~20% to ~80% at trial 20
    Expected patterns:
    - Pre-switch (W1-W4): Participants learn AI is bad → low/decreasing reliance → STAGNANT
    - Post-switch (W5-W6): AI becomes good but reliance may stay low → UNDER-RELIANCE
    - This maps to "AI Benefit Emergence" pattern from EdNet analysis!
    - Parasuraman & Riley (1997): "disuse" of a reliable system
    - Lee & Moray (1992): trust lags behind reliability changes (asymmetric)

  KEY HYPOTHESIS:
    → C1 should produce CATASTROPHIC + OSCILLATING patterns
    → C2 should produce AI BENEFIT EMERGENCE (under-adaptation) patterns
    → Both conditions should show CONVERGENT patterns (adaptive calibration)
    """)

    # --- 8. Trial-by-Trial Trajectories ---
    R.append("\n## 8. TRIAL-BY-TRIAL TRAJECTORY (group means)")
    for c, cl in [(1, 'High→Low'), (2, 'Low→High')]:
        R.append(f"\n### Condition {c} ({cl}):")
        R.append(f"  {'Trial':>5}  {'Follow':>7}  {'AI_acc':>7}  {'Correct':>7}  {'Gap':>7}")
        R.append(f"  {'-'*5}  {'-'*7}  {'-'*7}  {'-'*7}  {'-'*7}")
        for tr in range(1, 31):
            tt = [t for t in trials if t['condition'] == c and t['trial_num'] == tr]
            if not tt:
                continue
            fol = np.mean([t['followed_ai'] for t in tt])
            acc = np.mean([t['ai_accurate'] for t in tt])
            cor = np.mean([t['trial_correct'] for t in tt])
            gap = fol - acc
            marker = "  ◄ SWITCH" if tr == 21 else ""
            R.append(f"  {tr:>5}  {fol:>7.3f}  {acc:>7.3f}  {cor:>7.3f}  {gap:>+7.3f}{marker}")

    # --- 9. Over-Reliance Deep Dive (C1 post-switch) ---
    R.append("\n## 9. OVER-RELIANCE ANALYSIS (C1 Post-Switch)")
    c1_post = [t for t in trials if t['condition'] == 1 and t['phase'] == 'post_switch']
    if c1_post:
        followed_bad = [t for t in c1_post if t['followed_ai'] and not t['ai_accurate']]
        R.append(f"  Post-switch trials (C1): {len(c1_post)}")
        R.append(f"  Followed inaccurate AI: {len(followed_bad)} ({len(followed_bad)/len(c1_post)*100:.1f}%)")
        R.append(f"  → These are OVER-RELIANCE events (trust violation not yet processed)")
        hurt_count = sum(1 for t in followed_bad if t['ai_hurt'])
        R.append(f"  → Of these, AI actually hurt performance: {hurt_count} ({hurt_count/max(len(followed_bad),1)*100:.1f}%)")

    # --- 10. Under-Reliance Deep Dive (C2 post-switch) ---
    R.append("\n## 10. UNDER-RELIANCE / AI BENEFIT EMERGENCE (C2 Post-Switch)")
    c2_post = [t for t in trials if t['condition'] == 2 and t['phase'] == 'post_switch']
    if c2_post:
        ignored_good = [t for t in c2_post if not t['followed_ai'] and t['ai_accurate']]
        R.append(f"  Post-switch trials (C2): {len(c2_post)}")
        R.append(f"  Ignored accurate AI: {len(ignored_good)} ({len(ignored_good)/len(c2_post)*100:.1f}%)")
        R.append(f"  → These are UNDER-RELIANCE events (distrust persists despite good AI)")
        missed = sum(1 for t in ignored_good if not t['trial_correct'])
        R.append(f"  → Of these, participant got it wrong (missed opportunity): {missed} ({missed/max(len(ignored_good),1)*100:.1f}%)")

    return "\n".join(R)


# =============================================================================
# Utility
# =============================================================================
def _m(data, key):
    return np.mean([d[key] for d in data])


def _save_csv(path, data, columns):
    with open(path, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=columns, extrasaction='ignore')
        writer.writeheader()
        writer.writerows(data)
    print(f"Saved: {path} ({len(data)} rows)")


if __name__ == '__main__':
    main()
