import pandas as pd

def load_fire_data(path="data/raw/forestfires.csv"):
    df = pd.read_csv(path)
    return df

if __name__ == "__main__":
    df = load_fire_data()
    print(f"Loaded {len(df)} rows and {len(df.columns)} columns")
