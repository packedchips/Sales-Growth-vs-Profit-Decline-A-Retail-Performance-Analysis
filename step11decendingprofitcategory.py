import pandas as pd

df = pd.read_csv("sales.csv")

# Convert date
df["Order Date"] = pd.to_datetime(df["Order Date"], format="mixed", dayfirst=True)

# Create new columns
df["Month"] = df["Order Date"].dt.month
df["Year"] = df["Order Date"].dt.year

# discount vs profit by category with trend line
import numpy as np
import matplotlib.pyplot as plt

categories = df["Category"].unique()
for cat in categories:
    subset = df[df["Category"] == cat]
    analysis = subset.groupby("Discount")[["Profit"]].mean().reset_index()
    category = df.groupby("Category")[["Sales", "Profit"]].sum().reset_index()
    print(category.sort_values(by="Sales", ascending=False))

#from this we conclude that
#snacks contribute the second most to the profit but they also hurt the most by discounts 