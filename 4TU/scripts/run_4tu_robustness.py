from __future__ import annotations

import math
from pathlib import Path

import numpy as np
import pandas as pd
import statsmodels.formula.api as smf


SCRIPT_DIR = Path(__file__).resolve().parent
REPO_4TU = SCRIPT_DIR.parent
PROCESSED = REPO_4TU / "processed"
OUT = REPO_4TU / "manuscript" / "robustness_outputs"


BOOL_COLS = [
    "ai_wrong_by_design",
    "ai_correct",
    "initial_correct",
    "final_correct",
    "initial_agrees_ai",
    "final_follows_ai",
    "initial_disagreement",
    "switched",
    "switch_to_ai",
    "diagnostic_trial",
    "appropriate_reliance_all",
    "appropriate_reliance_diagnostic",
    "over_reliance",
    "under_reliance",
    "warranted_ai_reliance",
    "warranted_self_reliance",
]


def load_trials() -> pd.DataFrame:
    df = pd.read_csv(PROCESSED / "4tu_trial_level_calibration.csv")
    for col in BOOL_COLS:
        if col in df:
            if df[col].dtype == object:
                df[col] = df[col].map({"True": True, "False": False, True: True, False: False})
            df[col] = df[col].astype("boolean")
    return df


def as_numeric_bool(df: pd.DataFrame, cols: list[str]) -> pd.DataFrame:
    out = df.copy()
    for col in cols:
        out[col] = out[col].astype(int)
    return out


def tidy_glm(result, model_name: str, keep_terms: list[str]) -> pd.DataFrame:
    rows = []
    for term in keep_terms:
        if term not in result.params.index:
            continue
        b = float(result.params[term])
        se = float(result.bse[term])
        lo = b - 1.96 * se
        hi = b + 1.96 * se
        rows.append(
            {
                "model": model_name,
                "term": term,
                "b": b,
                "se_cluster_user": se,
                "or": math.exp(b),
                "or_ci_low": math.exp(lo),
                "or_ci_high": math.exp(hi),
                "p": float(result.pvalues[term]),
                "n": int(result.nobs),
            }
        )
    return pd.DataFrame(rows)


def fit_clustered_logit(formula: str, data: pd.DataFrame):
    model = smf.glm(formula=formula, data=data, family=__import__("statsmodels.api").api.families.Binomial())
    return model.fit(cov_type="cluster", cov_kwds={"groups": data["user_id"]})


def planned_contrast(result, label: str, contrast: str) -> dict:
    test = result.t_test(contrast)
    b = float(np.asarray(test.effect).ravel()[0])
    se = float(np.asarray(test.sd).ravel()[0])
    p = float(np.asarray(test.pvalue).ravel()[0])
    lo = b - 1.96 * se
    hi = b + 1.96 * se
    return {
        "contrast": label,
        "b": b,
        "se_cluster_user": se,
        "or": math.exp(b),
        "or_ci_low": math.exp(lo),
        "or_ci_high": math.exp(hi),
        "p": p,
    }


def prop_diff(x1: int, n1: int, x2: int, n2: int) -> dict:
    p1 = x1 / n1
    p2 = x2 / n2
    diff = p1 - p2
    se = math.sqrt(p1 * (1 - p1) / n1 + p2 * (1 - p2) / n2)
    lo = diff - 1.96 * se
    hi = diff + 1.96 * se
    z = diff / se if se else float("nan")
    # Normal approximation, two-sided.
    p = math.erfc(abs(z) / math.sqrt(2)) if se else float("nan")
    return {"diff": diff, "se": se, "ci_low": lo, "ci_high": hi, "z": z, "p": p}


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    trials = load_trials()
    main = trials[trials["study"] == "main_exp"].copy()

    diag = main[main["diagnostic_trial"] == True].dropna(subset=["appropriate_reliance_diagnostic"]).copy()
    diag = as_numeric_bool(diag, ["appropriate_reliance_diagnostic", "ai_correct"])

    primary = fit_clustered_logit(
        "appropriate_reliance_diagnostic ~ C(user_group, Treatment('system')) * ai_correct + task_position + C(task_id)",
        diag,
    )
    primary_terms = [
        "C(user_group, Treatment('system'))[T.accuracy]",
        "C(user_group, Treatment('system'))[T.analogy]",
        "ai_correct",
        "C(user_group, Treatment('system'))[T.accuracy]:ai_correct",
        "C(user_group, Treatment('system'))[T.analogy]:ai_correct",
        "task_position",
    ]
    tidy = [tidy_glm(primary, "Task-FE clustered appropriate reliance", primary_terms)]

    wrong = diag[diag["ai_correct"] == 0].copy()
    wrong["over_reliance"] = main.loc[wrong.index, "over_reliance"].astype(int)
    over = fit_clustered_logit(
        "over_reliance ~ C(user_group, Treatment('system')) + task_position + C(task_id)",
        wrong,
    )
    tidy.append(
        tidy_glm(
            over,
            "Task-FE clustered over-reliance",
            [
                "C(user_group, Treatment('system'))[T.accuracy]",
                "C(user_group, Treatment('system'))[T.analogy]",
                "task_position",
            ],
        )
    )

    correct = diag[diag["ai_correct"] == 1].copy()
    correct["under_reliance"] = main.loc[correct.index, "under_reliance"].astype(int)
    under = fit_clustered_logit(
        "under_reliance ~ C(user_group, Treatment('system')) + task_position + C(task_id)",
        correct,
    )
    tidy.append(
        tidy_glm(
            under,
            "Task-FE clustered under-reliance",
            [
                "C(user_group, Treatment('system'))[T.accuracy]",
                "C(user_group, Treatment('system'))[T.analogy]",
                "task_position",
            ],
        )
    )

    model_results = pd.concat(tidy, ignore_index=True)
    model_results.to_csv(OUT / "task_fe_clustered_model_results.csv", index=False)

    planned = []
    planned.append(
        planned_contrast(
            primary,
            "Appropriate reliance: accuracy vs system",
            "C(user_group, Treatment('system'))[T.accuracy] = 0",
        )
    )
    planned.append(
        planned_contrast(
            primary,
            "Appropriate reliance: analogy vs system",
            "C(user_group, Treatment('system'))[T.analogy] = 0",
        )
    )
    planned.append(
        planned_contrast(
            primary,
            "Appropriate reliance: analogy vs accuracy",
            "C(user_group, Treatment('system'))[T.analogy] - C(user_group, Treatment('system'))[T.accuracy] = 0",
        )
    )
    pd.DataFrame(planned).to_csv(OUT / "planned_condition_contrasts.csv", index=False)

    prop_rows = []
    for group, df in main.groupby("user_group"):
        d = df[df["diagnostic_trial"] == True]
        ai_correct = d[d["ai_correct"] == True]
        ai_wrong = d[d["ai_correct"] == False]
        rair_x = int(ai_correct["final_follows_ai"].sum())
        rair_n = len(ai_correct)
        rsr_x = int((~ai_wrong["final_follows_ai"].astype(bool)).sum())
        rsr_n = len(ai_wrong)
        contrast = prop_diff(rair_x, rair_n, rsr_x, rsr_n)
        prop_rows.append(
            {
                "group": group,
                "rair_x": rair_x,
                "rair_n": rair_n,
                "rsr_x": rsr_x,
                "rsr_n": rsr_n,
                "rair": rair_x / rair_n,
                "rsr": rsr_x / rsr_n,
                "rair_minus_rsr": contrast["diff"],
                "diff_ci_low": contrast["ci_low"],
                "diff_ci_high": contrast["ci_high"],
                "p_normal_approx": contrast["p"],
            }
        )
    pd.DataFrame(prop_rows).to_csv(OUT / "rair_rsr_difference_checks.csv", index=False)

    with (OUT / "README.md").open("w", encoding="utf-8") as f:
        f.write("# 4TU Robustness Outputs\n\n")
        f.write("Generated by `4TU/scripts/run_4tu_robustness.py`.\n\n")
        f.write("- `task_fe_clustered_model_results.csv`: logistic GLMs with task fixed effects and user-clustered standard errors.\n")
        f.write("- `planned_condition_contrasts.csv`: planned condition contrasts from the appropriate-reliance model.\n")
        f.write("- `rair_rsr_difference_checks.csv`: descriptive RAIR minus RSR checks using normal-approximation CIs.\n\n")
        f.write("These are robustness checks, not replacements for the lme4 mixed-effects baseline models.\n")

    print(OUT)


if __name__ == "__main__":
    main()
