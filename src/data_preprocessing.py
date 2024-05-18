import pandas as pd
from sklearn.model_selection import train_test_split

def preprocess_data():
    df = pd.read_csv('data/raw/boston_housing.csv')
    X = df.drop('PRICE', axis=1)
    y = df['PRICE']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    X_train.to_csv('data/processed/X_train.csv', index=False)
    X_test.to_csv('data/processed/X_test.csv', index=False)
    y_train.to_csv('data/processed/y_train.csv', index=False)
    y_test.to_csv('data/processed/y_test.csv', index=False)

if __name__ == "__main__":
    preprocess_data()
