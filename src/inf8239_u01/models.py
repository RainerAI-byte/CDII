from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.svm import SVC


def build_svm(C=1, gamma="scale"):

    numeric_columns = [
        "Attribute2",
        "Attribute5",
        "Attribute8",
        "Attribute11",
        "Attribute13",
        "Attribute16",
        "Attribute18",
    ]

    categorical_columns = [
        "Attribute1",
        "Attribute3",
        "Attribute4",
        "Attribute6",
        "Attribute7",
        "Attribute9",
        "Attribute10",
        "Attribute12",
        "Attribute14",
        "Attribute15",
        "Attribute17",
        "Attribute19",
        "Attribute20",
    ]

    numeric_pipeline = Pipeline([
        ("imputer", SimpleImputer(strategy="median")),
        ("scale", StandardScaler()),
    ])

    categorical_pipeline = Pipeline([
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("onehot", OneHotEncoder(handle_unknown="ignore")),
    ])

    preprocess = ColumnTransformer([
        ("num", numeric_pipeline, numeric_columns),
        ("cat", categorical_pipeline, categorical_columns),
    ])

    model = SVC(
        C=C,
        gamma=gamma,
        kernel="rbf",
        probability=True,
        random_state=42,
    )

    return Pipeline([
        ("prep", preprocess),
        ("model", model),
    ])