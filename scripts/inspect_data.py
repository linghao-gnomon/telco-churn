import pandas as pd
from pathlib import Path

source = Path("data/raw/telco.csv")

df = pd.read_csv(source)
print(df.shape)
print(df.dtypes)
print(df["Churn"].value_counts(dropna=False))