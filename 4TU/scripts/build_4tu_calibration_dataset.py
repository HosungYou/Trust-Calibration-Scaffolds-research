#!/usr/bin/env python3
"""Build trial-level trust/reliance calibration files for the 4TU loan dataset.

The source study stores participant decisions in long usertask tables and keeps
the task order plus intentionally wrong AI advice flags in userinfo.csv. This
script reconstructs a trial-level table that is easier to use for calibration
analyses.
"""

from __future__ import annotations

import re
from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[2]
DATA_ROOT = ROOT / "4TU" / "extracted" / "data"
OUT_DIR = ROOT / "4TU" / "processed"

MAIN_TASKS = [
    "LP001030",
    "LP001806",
    "LP002534",
    "LP001882",
    "LP002068",
    "LP001849",
    "LP002142",
    "LP001451",
    "LP002181",
    "LP002840",
]

FOLLOW_UP_TASKS = [
    "LP002571",
    "LP001633",
    "LP001882",
    "LP002181",
    "LP001469",
    "LP002500",
    "LP002449",
    "LP001722",
    "LP002534",
    "LP001451",
    "LP001536",
    "LP001996",
]


def reverse_answer(answer: str) -> str:
    if answer == "accept":
        return "reject"
    if answer == "reject":
        return "accept"
    raise ValueError(f"Unknown answer: {answer}")


def load_answer_key() -> dict[str, str]:
    """Load/reconstruct correct loan decisions.

    Main-study tasks are explicitly listed in selected_samples.csv. Follow-up
    added borderline tasks whose correct labels can be recovered from the
    positive/negative LR log files bundled with the dataset.
    """

    selection_dir = DATA_ROOT / "loan_data_selection"
    selected = pd.read_csv(selection_dir / "selected_samples.csv")
    answer_key = {
        row.Loan_ID: ("accept" if row.Loan_Status == "Y" else "reject")
        for row in selected.itertuples(index=False)
    }

    for filename, answer in [
        ("lr_reg_pos_ori_log.txt", "accept"),
        ("lr_reg_neg_ori_log.txt", "reject"),
    ]:
        text = (selection_dir / filename).read_text(encoding="utf-8")
        for loan_id in re.findall(r"LP\d{6}", text):
            answer_key.setdefault(loan_id, answer)

    missing = sorted(set(MAIN_TASKS + FOLLOW_UP_TASKS) - set(answer_key))
    if missing:
        raise RuntimeError(f"Missing answer labels for tasks: {missing}")
    return answer_key


def load_choice_lookup(study_dir: Path) -> dict[tuple[str, str, str], str]:
    usertask = pd.read_csv(study_dir / "anonymous_data" / "usertask.csv")
    usertask = usertask[usertask["answer_type"] != "attention"].copy()
    return {
        (row.user_id, row.task_id, row.answer_type): row.choice
        for row in usertask.itertuples(index=False)
    }


def add_trial_derivations(row: dict) -> dict:
    row["ai_correct"] = row["ai_advice"] == row["correct_answer"]
    row["initial_correct"] = row["initial_choice"] == row["correct_answer"]
    row["final_correct"] = row["final_choice"] == row["correct_answer"]
    row["initial_agrees_ai"] = row["initial_choice"] == row["ai_advice"]
    row["final_follows_ai"] = row["final_choice"] == row["ai_advice"]
    row["initial_disagreement"] = row["initial_choice"] != row["ai_advice"]
    row["switched"] = row["initial_choice"] != row["final_choice"]
    row["switch_to_ai"] = row["initial_disagreement"] and row["final_follows_ai"]
    row["diagnostic_trial"] = row["initial_disagreement"]

    # All-trial calibration state: useful descriptively, but diagnostic models
    # should usually restrict to initial_disagreement == True.
    row["appropriate_reliance_all"] = (
        (row["ai_correct"] and row["final_follows_ai"])
        or ((not row["ai_correct"]) and (not row["final_follows_ai"]))
    )

    if row["initial_disagreement"]:
        row["appropriate_reliance_diagnostic"] = row["final_correct"]
        row["over_reliance"] = (not row["ai_correct"]) and row["final_follows_ai"]
        row["under_reliance"] = row["ai_correct"] and (not row["final_follows_ai"])
        row["warranted_ai_reliance"] = row["ai_correct"] and row["final_follows_ai"]
        row["warranted_self_reliance"] = (not row["ai_correct"]) and (
            not row["final_follows_ai"]
        )
    else:
        row["appropriate_reliance_diagnostic"] = pd.NA
        row["over_reliance"] = pd.NA
        row["under_reliance"] = pd.NA
        row["warranted_ai_reliance"] = pd.NA
        row["warranted_self_reliance"] = pd.NA

    return row


def parse_bool_flags(flag_str: str) -> list[bool]:
    return [flag == "True" for flag in flag_str.split("|")]


def build_main_trials(answer_key: dict[str, str]) -> pd.DataFrame:
    study_dir = DATA_ROOT / "main_exp"
    userinfo = pd.read_csv(study_dir / "anonymous_data" / "userinfo.csv")
    choices = load_choice_lookup(study_dir)

    rows = []
    for user in userinfo.itertuples(index=False):
        tasks = user.task_order_str.split("|")
        flags = parse_bool_flags(user.reverse_flag_str)
        if len(tasks) != 10 or len(flags) != 10:
            raise RuntimeError(f"Unexpected main task order for {user.user_id}")

        for pos, (task_id, reverse_flag) in enumerate(zip(tasks, flags), start=1):
            correct = answer_key[task_id]
            ai_advice = reverse_answer(correct) if reverse_flag else correct
            try:
                initial_choice = choices[(user.user_id, task_id, "base")]
                final_choice = choices[(user.user_id, task_id, user.user_group)]
            except KeyError:
                continue
            row = {
                "study": "main_exp",
                "user_id": user.user_id,
                "user_group": user.user_group,
                "analogy_type": user.analogy_type if user.user_group == "analogy" else pd.NA,
                "analogy_domain": pd.NA,
                "task_id": task_id,
                "task_position": pos,
                "task_block": pd.NA,
                "correct_answer": correct,
                "ai_advice": ai_advice,
                "ai_wrong_by_design": reverse_flag,
                "initial_choice": initial_choice,
                "final_choice": final_choice,
            }
            rows.append(add_trial_derivations(row))
    return pd.DataFrame(rows)


def split_follow_up_order(task_order_str: str) -> tuple[list[str], list[str]]:
    task_str, analogy_str = task_order_str.strip().split(" ")
    tasks = task_str.split("|")
    analogies = analogy_str.split("|")
    if len(tasks) != 12 or len(analogies) != 3:
        raise RuntimeError(f"Unexpected follow-up task order: {task_order_str}")
    return tasks, analogies


def build_follow_up_trials(answer_key: dict[str, str]) -> pd.DataFrame:
    study_dir = DATA_ROOT / "follow_up_study"
    userinfo = pd.read_csv(study_dir / "anonymous_data" / "userinfo.csv")
    choices = load_choice_lookup(study_dir)

    rows = []
    for user in userinfo.itertuples(index=False):
        tasks, analogy_order = split_follow_up_order(user.task_order_str)
        flags = parse_bool_flags(user.reverse_flag_str)
        if len(flags) != 12:
            raise RuntimeError(f"Unexpected follow-up flags for {user.user_id}")

        for pos, (task_id, reverse_flag) in enumerate(zip(tasks, flags), start=1):
            correct = answer_key[task_id]
            ai_advice = reverse_answer(correct) if reverse_flag else correct
            block_index = (pos - 1) // 4
            analogy_domain = analogy_order[block_index]
            try:
                initial_choice = choices[(user.user_id, task_id, "base")]
                final_choice = choices[(user.user_id, task_id, "loan_analogy")]
            except KeyError:
                continue
            row = {
                "study": "follow_up_study",
                "user_id": user.user_id,
                "user_group": user.user_group,
                "analogy_type": user.analogy_type,
                "analogy_domain": analogy_domain,
                "task_id": task_id,
                "task_position": pos,
                "task_block": block_index + 1,
                "correct_answer": correct,
                "ai_advice": ai_advice,
                "ai_wrong_by_design": reverse_flag,
                "initial_choice": initial_choice,
                "final_choice": final_choice,
            }
            rows.append(add_trial_derivations(row))
    return pd.DataFrame(rows)


def summarize_participants(trials: pd.DataFrame) -> pd.DataFrame:
    grouped = trials.groupby(["study", "user_id"], dropna=False)
    rows = []
    for (study, user_id), df in grouped:
        diagnostic = df[df["diagnostic_trial"]]
        row = {
            "study": study,
            "user_id": user_id,
            "user_group": df["user_group"].iloc[0],
            "analogy_type": df["analogy_type"].iloc[0],
            "n_trials": len(df),
            "n_diagnostic_trials": len(diagnostic),
            "initial_accuracy": df["initial_correct"].mean(),
            "final_accuracy": df["final_correct"].mean(),
            "accuracy_gain": df["final_correct"].mean() - df["initial_correct"].mean(),
            "agreement_fraction": df["final_follows_ai"].mean(),
            "switching_fraction": diagnostic["switch_to_ai"].mean()
            if len(diagnostic)
            else pd.NA,
            "appropriate_reliance_diagnostic": diagnostic[
                "appropriate_reliance_diagnostic"
            ].mean()
            if len(diagnostic)
            else pd.NA,
            "over_reliance_rate": diagnostic["over_reliance"].mean()
            if len(diagnostic)
            else pd.NA,
            "under_reliance_rate": diagnostic["under_reliance"].mean()
            if len(diagnostic)
            else pd.NA,
            "reliance_sensitivity": (
                diagnostic.loc[diagnostic["ai_correct"], "final_follows_ai"].mean()
                - diagnostic.loc[~diagnostic["ai_correct"], "final_follows_ai"].mean()
            )
            if len(diagnostic)
            else pd.NA,
        }
        rows.append(row)
    return pd.DataFrame(rows)


def write_profile(trials: pd.DataFrame, participants: pd.DataFrame) -> None:
    def md_table(df: pd.DataFrame) -> str:
        if df.empty:
            return "_No rows._"
        rendered = df.fillna("").astype(str)
        headers = list(rendered.columns)
        rows = rendered.values.tolist()
        sep = ["---"] * len(headers)
        lines = [
            "| " + " | ".join(headers) + " |",
            "| " + " | ".join(sep) + " |",
        ]
        lines.extend("| " + " | ".join(row) + " |" for row in rows)
        return "\n".join(lines)

    lines = [
        "# 4TU Trust/ Reliance Calibration Data Profile",
        "",
        "Generated by `4TU/scripts/build_4tu_calibration_dataset.py`.",
        "",
        "## Row Counts",
        "",
        trials.groupby(["study", "user_group"], dropna=False)
        .size()
        .rename("trials")
        .reset_index()
        .pipe(md_table),
        "",
        "## Diagnostic Trial Counts",
        "",
        trials.groupby(["study", "user_group", "diagnostic_trial"], dropna=False)
        .size()
        .rename("trials")
        .reset_index()
        .pipe(md_table),
        "",
        "## Participant-Level Means",
        "",
        participants.groupby(["study", "user_group"], dropna=False)[
            [
                "n_diagnostic_trials",
                "initial_accuracy",
                "final_accuracy",
                "accuracy_gain",
                "agreement_fraction",
                "switching_fraction",
                "appropriate_reliance_diagnostic",
                "over_reliance_rate",
                "under_reliance_rate",
                "reliance_sensitivity",
            ]
        ]
        .mean(numeric_only=True)
        .round(3)
        .reset_index()
        .pipe(md_table),
        "",
        "## Measurement Note",
        "",
        "- `final_follows_ai` is observable agreement with the AI advice.",
        "- `switch_to_ai` is the cleaner reliance measure because it is limited to trials where the participant initially disagreed with the AI.",
        "- `appropriate_reliance_diagnostic` equals final correctness on diagnostic trials; it separates over-reliance on wrong AI advice from under-reliance on correct AI advice.",
        "- Participant-level `reliance_sensitivity` is `P(follow AI | AI correct) - P(follow AI | AI wrong)` within diagnostic trials.",
    ]
    (OUT_DIR / "data_profile.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    answer_key = load_answer_key()
    main_trials = build_main_trials(answer_key)
    follow_up_trials = build_follow_up_trials(answer_key)
    trials = pd.concat([main_trials, follow_up_trials], ignore_index=True)
    participants = summarize_participants(trials)

    trials.to_csv(OUT_DIR / "4tu_trial_level_calibration.csv", index=False)
    participants.to_csv(OUT_DIR / "4tu_participant_summary_calibration.csv", index=False)
    write_profile(trials, participants)

    print(f"Wrote {len(trials):,} trial rows")
    print(f"Wrote {len(participants):,} participant rows")
    print(f"Output directory: {OUT_DIR}")


if __name__ == "__main__":
    main()
