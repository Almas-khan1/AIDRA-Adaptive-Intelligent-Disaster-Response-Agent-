import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score


class MLModule:

    def __init__(self, path):

        self.data = pd.read_csv(path)

        self.le = LabelEncoder()
        self.scaler = StandardScaler()

    def preprocess(self):

        self.data["arrival_mode"] = self.le.fit_transform(
            self.data["arrival_mode"]
        )

        X = self.data.drop("triage_level", axis=1)
        y = self.data["triage_level"]

        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )

        X_train = self.scaler.fit_transform(X_train)
        X_test = self.scaler.transform(X_test)

        return X_train, X_test, y_train, y_test

    def run(self):

        X_train, X_test, y_train, y_test = self.preprocess()

        models = {
            "KNN": KNeighborsClassifier(5),
            "NB": GaussianNB()
        }

        results = {}

        for name, model in models.items():

            model.fit(X_train, y_train)
            pred = model.predict(X_test)

            results[name] = accuracy_score(y_test, pred)

        return results