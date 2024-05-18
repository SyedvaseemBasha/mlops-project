import pandas as pd
from sklearn.datasets import load_boston

def ingest_data():
    boston = load_boston()
    df = pd.DataFrame(boston.data, columns=boston.feature_names)
    df['PRICE'] = boston.target
    df.to_csv('data/raw/boston_housing.csv', index=False)

if __name__ == "__main__":
    ingest_data()

