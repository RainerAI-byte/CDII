from pathlib import Path

import pandas as pd

from src.inf8239_u01.data import download_csv


TARGET = "Target"

REQUIRED = {
    TARGET,
    "Marital Status",
    "Course",
}

URL = "https://archive.ics.uci.edu/static/public/697/data.csv"
DATA_PATH = Path("data/raw/dataset.csv")


def load_data():
    if not DATA_PATH.exists():
        download_csv(URL, DATA_PATH)

    return pd.read_csv(DATA_PATH)


def test_dataset_is_not_empty():
    assert not load_data().empty


def test_required_columns_exist():
    assert REQUIRED <= set(load_data().columns)


def test_target_has_no_missing_and_three_classes():
    y = load_data()[TARGET]

    assert y.notna().all()
    assert y.nunique() >= 2