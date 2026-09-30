import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score

from inf8239_u01.models import build_svm


DATA_PATH = "data/raw/dataset.csv"
TARGET = "class"


def load_data():
    df = pd.read_csv(DATA_PATH)

    X = df.drop(columns=[TARGET])
    y = df[TARGET]

    return X, y


def test_svm_returns_one_prediction_per_row():
    X, y = load_data()

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=42,
        stratify=y
    )

    model = build_svm()

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    assert len(predictions) == len(y_test)


def test_svm_produces_two_classes():
    X, y = load_data()

    model = build_svm()

    model.fit(X, y)

    predictions = model.predict(X)

    assert len(set(predictions)) >= 2


def test_svm_f1_macro_is_valid():
    X, y = load_data()

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=42,
        stratify=y
    )

    model = build_svm()

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    score = f1_score(
        y_test,
        predictions,
        average="macro"
    )

    assert 0 <= score <= 1