
import pandas as pd
import pytest

from sklearn.model_selection import train_test_split

from src.train_models import (
    load_data,
    build_models,
    evaluate_model,
    RANDOM_STATE,
)


def test_dataset_is_not_empty():
    """1. El dataset debe contener registros."""
    df = load_data()
    assert len(df) > 0


def test_dataset_has_required_columns():
    """2. Deben existir las columnas necesarias."""
    df = load_data()
    assert {"message", "label"}.issubset(df.columns)


def test_labels_are_valid():
    """3. Solo aceptamos ham y spam."""
    df = load_data()
    assert set(df["label"].unique()) == {"ham", "spam"}


def test_no_missing_or_empty_messages():
    """4. Los mensajes y etiquetas deben estar completos."""
    df = load_data()
    assert not df["message"].isna().any()
    assert not df["label"].isna().any()
    assert df["message"].str.strip().ne("").all()


def test_no_duplicate_messages():
    """5. No debe haber mensajes repetidos tras la limpieza."""
    df = load_data()
    assert not df["message"].duplicated().any()


def test_split_is_reproducible_and_has_expected_size():
    """6. La partición debe ser repetible y conservar el 20 % de prueba."""
    df = load_data()

    X = df["message"]
    y = df["label"]

    split1 = train_test_split(
        X, y,
        test_size=0.20,
        random_state=RANDOM_STATE,
        stratify=y,
    )

    split2 = train_test_split(
        X, y,
        test_size=0.20,
        random_state=RANDOM_STATE,
        stratify=y,
    )

    X_train1, X_test1, y_train1, y_test1 = split1
    X_train2, X_test2, y_train2, y_test2 = split2

    assert len(X_test1) == pytest.approx(len(df) * 0.20, abs=1)
    assert X_train1.equals(X_train2)
    assert X_test1.equals(X_test2)
    assert y_train1.equals(y_train2)
    assert y_test1.equals(y_test2)


def test_model_catalog_contains_three_models():
    """7. Debemos tener baseline y dos candidatos."""
    models = build_models()

    assert set(models) == {
        "baseline",
        "naive_bayes",
        "logistic_regression",
    }


def test_model_evaluation_returns_valid_metrics():
    """8. El modelo debe entrenarse y devolver métricas válidas."""
    X_train = pd.Series([
        "meeting schedule for tomorrow",
        "project report and meeting notes",
        "free prize claim your reward now",
        "winner selected claim your cash prize",
        "team meeting at the office",
        "urgent offer win a free prize",
        "please review the project report",
        "claim your free reward immediately",
    ])

    y_train = pd.Series([
        "ham", "ham", "spam", "spam",
        "ham", "spam", "ham", "spam",
    ])

    X_test = pd.Series([
        "meeting report",
        "claim your free prize",
        "office schedule",
        "win cash reward",
    ])

    y_test = pd.Series(["ham", "spam", "ham", "spam"])

    model = build_models()["naive_bayes"]

    result = evaluate_model(
        "naive_bayes",
        model,
        X_train,
        X_test,
        y_train,
        y_test,
    )

    assert 0 <= result["precision_spam"] <= 1
    assert 0 <= result["recall_spam"] <= 1
    assert 0 <= result["f1_macro"] <= 1
    assert 0 <= result["pr_auc_average_precision"] <= 1
    assert result["train_seconds"] >= 0


def test_train_and_test_messages_do_not_overlap():
    """Comprueba que no haya mensajes compartidos entre entrenamiento y prueba."""
    from sklearn.model_selection import train_test_split

    df = load_data()

    X_train, X_test, _, _ = train_test_split(
        df["message"],
        df["label"],
        test_size=0.20,
        random_state=RANDOM_STATE,
        stratify=df["label"],
    )

    assert set(X_train).isdisjoint(set(X_test))

def test_demo_predict_email_returns_valid_label():
    """Comprueba que la demo devuelve una etiqueta válida."""
    from demo.predict_email import load_model, predict_email

    model = load_model()
    prediction, probability = predict_email(
        model,
        "Hello, the meeting is scheduled for tomorrow at 10 AM."
    )

    assert prediction in {"ham", "spam"}


def test_demo_predict_email_returns_valid_probability():
    """Comprueba que la probabilidad estimada está entre 0 y 1."""
    from demo.predict_email import load_model, predict_email

    model = load_model()
    _, probability = predict_email(
        model,
        "Congratulations! You have won a free prize. Click here now!"
    )

    assert probability is not None
    assert 0.0 <= probability <= 1.0


def test_demo_predict_email_rejects_empty_message():
    """Comprueba que la demo rechaza mensajes vacíos."""
    import pytest
    from demo.predict_email import load_model, predict_email

    model = load_model()

    with pytest.raises(ValueError, match="vacío"):
        predict_email(model, "   ")

