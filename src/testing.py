import pandas as pd
import numpy as np  

df = pd.read_csv("data/output(1).csv")

print(df.iloc[:, :11].head().to_string())

