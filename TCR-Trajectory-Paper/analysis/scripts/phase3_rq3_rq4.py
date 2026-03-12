"""
Phase 3: RQ3 (early behavior prediction) + RQ4 (class-outcome comparison)

RQ3: Can early behavior predict trajectory class membership?
  → Multinomial logistic regression: early features → class

RQ4: Do trajectory classes differ in learning outcomes?
  → ANOVA / Kruskal-Wallis on overall accuracy and improvement

Input:
  - phase1_early_behavior.csv
  - phase1_student_summary.csv
  - phase1_timeseries_long.csv
  - phase2_class_assignments.csv

Output:
  - phase3_rq3_prediction.csv (model coefficients + classification report)
  - phase3_rq4_outcomes.csv (class-level outcome statistics)
  - phase3_summary.txt (human-readable summary)
"""

import csv
import sys
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats

OUT_DIR = Path("/Volumes/External SSD/Projects/Research/Trust-Calibration-Scaffolds-research/"
               "TCR-Trajectory-Paper/analysis/outputs")

# ── Load data ──
print("Loading data...")
early = pd.read_csv(OUT_DIR / "phase1_early_behavior.csv")
summary = pd.read_csv(OUT_DIR / "phase1_student_summary.csv")
ts = pd.read_csv(OUT_DIR / "phase1_timeseries_long.csv")
classes = pd.read_csv(OUT_DIR / "phase2_class_assignments.csv")

# Merge class assignments with student data
df = summary.merge(classes[["user_id", "class", "uncertainty"]], on="user_id")
df = df.merge(early, on="user_id")

print(f"N = {len(df)}, Classes = {sorted(df['class'].unique())}")

# ── Compute outcome variables ──
# Learning improvement: accuracy in last 2 windows - first 2 windows
first2 = ts[ts["window"] <= 2].groupby("user_id").agg(
    early_acc=("P", "mean"),
    early_rb=("R_b", "mean")
).reset_index()

last2 = ts[ts["window"] >= 9].groupby("user_id").agg(
    late_acc=("P", "mean"),
    late_rb=("R_b", "mean")
).reset_index()

outcomes = first2.merge(last2, on="user_id")
outcomes["acc_improvement"] = outcomes["late_acc"] - outcomes["early_acc"]
outcomes["rb_improvement"] = outcomes["late_rb"] - outcomes["early_rb"]

df = df.merge(outcomes, on="user_id")

# ══════════════════════════════════════════════════
# RQ3: Early Behavior → Class Prediction
# ══════════════════════════════════════════════════
print("\n" + "=" * 60)
print("RQ3: EARLY BEHAVIOR PREDICTION")
print("=" * 60)

try:
    from sklearn.linear_model import LogisticRegression
    from sklearn.preprocessing import StandardScaler
    from sklearn.model_selection import cross_val_predict, StratifiedKFold
    from sklearn.metrics import classification_report, accuracy_score
    HAS_SKLEARN = True
except ImportError:
    HAS_SKLEARN = False
    print("WARNING: scikit-learn not available. Skipping RQ3 prediction model.")

if HAS_SKLEARN:
    features = [
        "early_R_b", "early_P", "early_gap",
        "early_expl_rate", "early_avg_expl_dur_s",
        "early_lecture_rate", "early_answer_change_rate"
    ]

    X = df[features].values
    y = df["class"].values

    # Handle NaN/inf
    X = np.nan_to_num(X, nan=0.0, posinf=0.0, neginf=0.0)

    # Standardize
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Multinomial logistic regression with 10-fold CV
    lr = LogisticRegression(max_iter=1000, random_state=42)
    cv = StratifiedKFold(n_splits=10, shuffle=True, random_state=42)
    y_pred = cross_val_predict(lr, X_scaled, y, cv=cv)

    acc = accuracy_score(y, y_pred)
    print(f"\n10-Fold CV Accuracy: {acc:.4f}")
    print(f"Chance level: {1/len(np.unique(y)):.4f}")
    print(f"\nClassification Report:")
    report = classification_report(y, y_pred, output_dict=True)
    print(classification_report(y, y_pred))

    # Fit on full data for coefficients
    lr_full = LogisticRegression(max_iter=1000, random_state=42)
    lr_full.fit(X_scaled, y)

    print("Feature importance (absolute mean coefficient across classes):")
    coef_importance = np.abs(lr_full.coef_).mean(axis=0)
    for feat, imp in sorted(zip(features, coef_importance), key=lambda x: -x[1]):
        print(f"  {feat:30s}: {imp:.4f}")

    # Save prediction results
    pred_df = pd.DataFrame({
        "feature": features,
        "mean_abs_coef": coef_importance
    }).sort_values("mean_abs_coef", ascending=False)
    pred_df.to_csv(OUT_DIR / "phase3_rq3_prediction.csv", index=False)
    print(f"\nSaved: phase3_rq3_prediction.csv")


# ══════════════════════════════════════════════════
# RQ4: Class → Learning Outcomes
# ══════════════════════════════════════════════════
print("\n" + "=" * 60)
print("RQ4: CLASS-OUTCOME COMPARISON")
print("=" * 60)

# Overall accuracy by class
print("\n--- Overall Accuracy by Class ---")
class_stats = []
for cls in sorted(df["class"].unique()):
    cls_data = df[df["class"] == cls]
    class_stats.append({
        "class": cls,
        "n": len(cls_data),
        "pct": len(cls_data) / len(df) * 100,
        "overall_acc_mean": cls_data["overall_accuracy"].mean(),
        "overall_acc_sd": cls_data["overall_accuracy"].std(),
        "acc_improve_mean": cls_data["acc_improvement"].mean(),
        "acc_improve_sd": cls_data["acc_improvement"].std(),
        "rb_improve_mean": cls_data["rb_improvement"].mean(),
        "rb_improve_sd": cls_data["rb_improvement"].std(),
        "time_span_mean": cls_data["time_span_days"].mean(),
        "n_episodes_mean": cls_data["n_episodes"].mean(),
        "adaptive_ratio_mean": cls_data["adaptive_ratio"].mean(),
        "uncertainty_mean": cls_data["uncertainty"].mean(),
    })

stats_df = pd.DataFrame(class_stats)
print(stats_df.to_string(index=False, float_format="%.4f"))

# ANOVA: overall accuracy
print("\n--- ANOVA: Overall Accuracy ---")
groups_acc = [df[df["class"] == c]["overall_accuracy"].values for c in sorted(df["class"].unique())]
f_acc, p_acc = stats.f_oneway(*groups_acc)
print(f"  F({len(groups_acc)-1}, {len(df)-len(groups_acc)}) = {f_acc:.4f}, p = {p_acc:.2e}")

# Effect size (eta-squared)
ss_between = sum(len(g) * (g.mean() - df["overall_accuracy"].mean())**2 for g in groups_acc)
ss_total = sum((df["overall_accuracy"] - df["overall_accuracy"].mean())**2)
eta_sq = ss_between / ss_total
print(f"  η² = {eta_sq:.4f}")

# Kruskal-Wallis (non-parametric alternative)
h_acc, p_kw = stats.kruskal(*groups_acc)
print(f"  Kruskal-Wallis H = {h_acc:.4f}, p = {p_kw:.2e}")

# ANOVA: accuracy improvement
print("\n--- ANOVA: Accuracy Improvement (late - early) ---")
groups_imp = [df[df["class"] == c]["acc_improvement"].values for c in sorted(df["class"].unique())]
f_imp, p_imp = stats.f_oneway(*groups_imp)
print(f"  F = {f_imp:.4f}, p = {p_imp:.2e}")

ss_between_imp = sum(len(g) * (g.mean() - df["acc_improvement"].mean())**2 for g in groups_imp)
ss_total_imp = sum((df["acc_improvement"] - df["acc_improvement"].mean())**2)
eta_sq_imp = ss_between_imp / ss_total_imp
print(f"  η² = {eta_sq_imp:.4f}")

# ANOVA: reliance change
print("\n--- ANOVA: Reliance Change (late R_b - early R_b) ---")
groups_rb = [df[df["class"] == c]["rb_improvement"].values for c in sorted(df["class"].unique())]
f_rb, p_rb = stats.f_oneway(*groups_rb)
print(f"  F = {f_rb:.4f}, p = {p_rb:.2e}")

# Post-hoc pairwise comparisons (Tukey HSD for overall accuracy)
print("\n--- Post-hoc: Tukey HSD (Overall Accuracy) ---")
from itertools import combinations
classes_sorted = sorted(df["class"].unique())
sig_pairs = []
for c1, c2 in combinations(classes_sorted, 2):
    g1 = df[df["class"] == c1]["overall_accuracy"]
    g2 = df[df["class"] == c2]["overall_accuracy"]
    t_stat, p_val = stats.ttest_ind(g1, g2)
    # Bonferroni correction
    n_comparisons = len(list(combinations(classes_sorted, 2)))
    p_adj = min(p_val * n_comparisons, 1.0)
    d = (g1.mean() - g2.mean()) / np.sqrt((g1.std()**2 + g2.std()**2) / 2)  # Cohen's d
    sig = "***" if p_adj < 0.001 else "**" if p_adj < 0.01 else "*" if p_adj < 0.05 else "ns"
    if p_adj < 0.05:
        sig_pairs.append((c1, c2, d, p_adj))
    print(f"  Class {c1} vs {c2}: d={d:+.3f}, p_adj={p_adj:.4f} {sig}")

# Save outcomes
stats_df.to_csv(OUT_DIR / "phase3_rq4_outcomes.csv", index=False)
print(f"\nSaved: phase3_rq4_outcomes.csv")

# ══════════════════════════════════════════════════
# Summary
# ══════════════════════════════════════════════════
print("\n" + "=" * 60)
print("PHASE 3 SUMMARY")
print("=" * 60)

if HAS_SKLEARN:
    print(f"\nRQ3: Early behavior predicts trajectory class")
    print(f"  10-fold CV accuracy: {acc:.4f} (chance: {1/len(np.unique(y)):.4f})")
    print(f"  Top predictors: {pred_df.iloc[0]['feature']}, {pred_df.iloc[1]['feature']}")

print(f"\nRQ4: Classes differ in learning outcomes")
print(f"  Overall accuracy: F={f_acc:.2f}, p={p_acc:.2e}, η²={eta_sq:.4f}")
print(f"  Accuracy improvement: F={f_imp:.2f}, p={p_imp:.2e}, η²={eta_sq_imp:.4f}")

# Rank classes by overall accuracy
ranked = stats_df.sort_values("overall_acc_mean", ascending=False)
print(f"\n  Classes ranked by overall accuracy:")
for _, row in ranked.iterrows():
    print(f"    Class {int(row['class'])}: {row['overall_acc_mean']:.4f} "
          f"(N={int(row['n'])}, improve={row['acc_improve_mean']:+.4f})")

# Write summary text
with open(OUT_DIR / "phase3_summary.txt", "w") as f:
    f.write("Phase 3 Summary: RQ3 + RQ4\n")
    f.write("=" * 50 + "\n\n")
    if HAS_SKLEARN:
        f.write(f"RQ3: 10-fold CV accuracy = {acc:.4f} (chance = {1/len(np.unique(y)):.4f})\n")
        f.write(f"Top predictors:\n")
        for _, row in pred_df.iterrows():
            f.write(f"  {row['feature']}: {row['mean_abs_coef']:.4f}\n")
    f.write(f"\nRQ4:\n")
    f.write(f"  Overall accuracy ANOVA: F={f_acc:.4f}, p={p_acc:.2e}, η²={eta_sq:.4f}\n")
    f.write(f"  Accuracy improvement ANOVA: F={f_imp:.4f}, p={p_imp:.2e}, η²={eta_sq_imp:.4f}\n")
    f.write(f"\nClass rankings (overall accuracy):\n")
    for _, row in ranked.iterrows():
        f.write(f"  Class {int(row['class'])}: acc={row['overall_acc_mean']:.4f}, "
                f"improve={row['acc_improve_mean']:+.4f}, N={int(row['n'])}\n")

print("\nSaved: phase3_summary.txt")
print("\n============ Phase 3 Complete ============")
