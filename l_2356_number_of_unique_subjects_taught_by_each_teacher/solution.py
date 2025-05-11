import pandas as pd

def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    dist_subjs = teacher.groupby("teacher_id")["subject_id"].unique().reset_index()
    return dist_subjs.rename(columns={"subject_id": "cnt"})
