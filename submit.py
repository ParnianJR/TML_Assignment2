from pathlib import Path

import pandas as pd
import requests

BASE_URL = "http://34.63.153.158"
TASK_ID = "19-stolen-model-detection"
API_KEY = "Your API key here"

FILE_PATH = Path(__file__).resolve().parent / "submission.csv"


def validate_submission(df: pd.DataFrame) -> None:
    if df.empty:
        raise ValueError("submission.csv is empty")


def main() -> None:
    if not API_KEY :
        raise RuntimeError("Set your API key in the API_KEY variable before submitting.")

    if not FILE_PATH.exists():
        raise FileNotFoundError(f"Submission file does not exist: {FILE_PATH}")

    submission_for_check = pd.read_csv(FILE_PATH)
    validate_submission(submission_for_check)

    with open(FILE_PATH, "rb") as submission_file:
        response = requests.post(
            f"{BASE_URL}/submit/{TASK_ID}",
            headers={"X-API-Key": API_KEY},
            files={"file": (FILE_PATH.name, submission_file, "text/csv")},
            timeout=(10, 120),
        )

    response.raise_for_status()
    print("Submission response:", response.json())


if __name__ == "__main__":
    main()