#!/usr/bin/env Rscript

suppressPackageStartupMessages({
  library(lme4)
})

args_file <- sub("^--file=", "", grep("^--file=", commandArgs(FALSE), value = TRUE))
if (length(args_file) == 1 && nzchar(args_file)) {
  repo_root <- normalizePath(file.path(dirname(args_file), "..", ".."))
} else {
  repo_root <- normalizePath(".")
}
processed_dir <- file.path(repo_root, "4TU", "processed")
out_dir <- file.path(repo_root, "4TU", "processed", "model_outputs")
dir.create(out_dir, recursive = TRUE, showWarnings = FALSE)

trial_path <- file.path(processed_dir, "4tu_trial_level_calibration.csv")
participant_path <- file.path(processed_dir, "4tu_participant_summary_calibration.csv")

trials <- read.csv(trial_path, stringsAsFactors = FALSE)
participants <- read.csv(participant_path, stringsAsFactors = FALSE)

as_bool <- function(x) {
  if (is.logical(x)) return(x)
  ifelse(x %in% c("True", "TRUE", "true"), TRUE,
         ifelse(x %in% c("False", "FALSE", "false"), FALSE, NA))
}

bool_cols <- c(
  "ai_wrong_by_design", "ai_correct", "initial_correct", "final_correct",
  "initial_agrees_ai", "final_follows_ai", "initial_disagreement", "switched",
  "switch_to_ai", "diagnostic_trial", "appropriate_reliance_all",
  "appropriate_reliance_diagnostic", "over_reliance", "under_reliance",
  "warranted_ai_reliance", "warranted_self_reliance"
)
for (col in intersect(bool_cols, names(trials))) {
  trials[[col]] <- as_bool(trials[[col]])
}

trials$user_group <- factor(trials$user_group)
trials$user_group <- relevel(trials$user_group, ref = "system")
trials$analogy_domain <- factor(trials$analogy_domain)
trials$user_id <- factor(trials$user_id)
trials$task_id <- factor(trials$task_id)

write_table <- function(df, filename) {
  write.csv(df, file.path(out_dir, filename), row.names = FALSE)
}

capture_model <- function(model, filename) {
  capture.output(summary(model), file = file.path(out_dir, filename))
}

rate <- function(x) mean(x, na.rm = TRUE)

main_desc <- aggregate(
  cbind(
    final_follows_ai,
    switch_to_ai,
    appropriate_reliance_diagnostic,
    over_reliance,
    under_reliance,
    final_correct
  ) ~ study + user_group + diagnostic_trial + ai_correct,
  data = trials,
  FUN = rate
)
write_table(main_desc, "descriptive_rates_by_condition.csv")

diagnostic_main <- subset(
  trials,
  study == "main_exp" & diagnostic_trial == TRUE &
    !is.na(appropriate_reliance_diagnostic)
)
diagnostic_main$user_group <- droplevels(diagnostic_main$user_group)

model_primary <- glmer(
  appropriate_reliance_diagnostic ~ user_group * ai_correct + task_position +
    (1 | user_id) + (1 | task_id),
  data = diagnostic_main,
  family = binomial,
  control = glmerControl(optimizer = "bobyqa")
)
capture_model(model_primary, "model_1_main_appropriate_reliance.txt")

main_wrong_ai <- subset(diagnostic_main, ai_correct == FALSE & !is.na(over_reliance))
model_over <- glmer(
  over_reliance ~ user_group + task_position + (1 | user_id) + (1 | task_id),
  data = main_wrong_ai,
  family = binomial,
  control = glmerControl(optimizer = "bobyqa")
)
capture_model(model_over, "model_2_main_over_reliance_wrong_ai.txt")

main_correct_ai <- subset(diagnostic_main, ai_correct == TRUE & !is.na(under_reliance))
model_under <- glmer(
  under_reliance ~ user_group + task_position + (1 | user_id) + (1 | task_id),
  data = main_correct_ai,
  family = binomial,
  control = glmerControl(optimizer = "bobyqa")
)
capture_model(model_under, "model_3_main_under_reliance_correct_ai.txt")

follow_diag <- subset(
  trials,
  study == "follow_up_study" & diagnostic_trial == TRUE &
    !is.na(appropriate_reliance_diagnostic)
)
follow_diag$analogy_domain <- relevel(droplevels(follow_diag$analogy_domain), ref = "train")

model_follow <- glmer(
  appropriate_reliance_diagnostic ~ analogy_domain * ai_correct + task_block +
    (1 | user_id) + (1 | task_id),
  data = follow_diag,
  family = binomial,
  control = glmerControl(optimizer = "bobyqa")
)
capture_model(model_follow, "model_4_followup_analogy_domain.txt")

participant_rates <- aggregate(
  cbind(
    n_diagnostic_trials,
    initial_accuracy,
    final_accuracy,
    accuracy_gain,
    agreement_fraction,
    switching_fraction,
    appropriate_reliance_diagnostic,
    over_reliance_rate,
    under_reliance_rate,
    reliance_sensitivity
  ) ~ study + user_group,
  data = participants,
  FUN = function(x) mean(x, na.rm = TRUE)
)
write_table(participant_rates, "participant_level_rates.csv")

sink(file.path(out_dir, "README_model_outputs.txt"))
cat("4TU baseline model outputs\n")
cat("==========================\n\n")
cat("Generated from 4TU/processed/4tu_trial_level_calibration.csv\n\n")
cat("Files:\n")
cat("- descriptive_rates_by_condition.csv\n")
cat("- participant_level_rates.csv\n")
cat("- model_1_main_appropriate_reliance.txt\n")
cat("- model_2_main_over_reliance_wrong_ai.txt\n")
cat("- model_3_main_under_reliance_correct_ai.txt\n")
cat("- model_4_followup_analogy_domain.txt\n\n")
cat("Primary interpretation should focus on diagnostic trials where initial_choice != ai_advice.\n")
cat("Use the models as baseline checks; refine with planned contrasts and robustness checks before manuscript use.\n")
sink()

cat("Wrote model outputs to ", out_dir, "\n", sep = "")
