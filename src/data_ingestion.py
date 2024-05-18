import pandas as pd
# from sklearn.datasets import load_boston
from sklearn.datasets import fetch_california_housing
    

def ingest_data():
    housing = fetch_california_housing()
    df = pd.DataFrame(housing.data, columns=housing.feature_names)
    df['PRICE'] = housing.target
    df.to_csv('data/raw/boston_housing.csv', index=False)

if __name__ == "__main__":
    ingest_data()


