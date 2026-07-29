import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from statsmodels.distributions.empirical_distribution import ECDF


df = pd.read_csv("data/Cleaned_sheet.csv")

df["Date"] = pd.to_datetime(df["Date"])

print(df.sort_values(["WD EID", "Emp Name", "Date"], ascending=[True, True, True])[df["Emp Name"] == "Nguyen Duc Thuan"])