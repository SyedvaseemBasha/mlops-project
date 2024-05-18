import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib
import mlflow
import mlflow.sklearn

def train_model():
    mlflow.start_run()

    X_train = pd.read_csv('data/processed/X_train.csv')
    y_train = pd.read_csv('data/processed/y_train.csv')

    model = LinearRegression()
    model.fit(X_train, y_train)

    joblib.dump(model, 'models/house_price_model.pkl')
    mlflow.sklearn.log_model(model, "model")
    mlflow.log_param("model_type", "LinearRegression")
    mlflow.log_metric("training_score", model.score(X_train, y_train))

    mlflow.end_run()

if __name__ == "__main__":
    train_model()
