import pandas as pd

df = pd.read_csv("sales.csv")

# Convert date
df["Order Date"] = pd.to_datetime(df["Order Date"], format="mixed", dayfirst=True)

# Create new columns
df["Month"] = df["Order Date"].dt.month
df["Year"] = df["Order Date"].dt.year

# Profit Margin
df["Profit Margin"] = df["Profit"] / df["Sales"]

# Group by month and year
monthly = df.groupby(["Year", "Month"])[["Sales", "Profit"]].sum().reset_index()
print(monthly.head())