import pandas as pd

df = pd.read_csv("sales.csv")

# Convert date
df["Order Date"] = pd.to_datetime(df["Order Date"], format="mixed", dayfirst=True)

# Create new columns
df["Month"] = df["Order Date"].dt.month
df["Year"] = df["Order Date"].dt.year

import matplotlib.pyplot as plt
region = df.groupby("Region")[["Sales", "Profit"]].sum()
print(region)
region["Profit Margin"] = region["Profit"] / region ["Sales"]
print(region)

import matplotlib.pyplot as plt

# Sales & Profit
region[["Sales", "Profit"]].plot(kind="bar")
plt.title("Sales vs Profit by Region")
plt.xticks(rotation=45)
plt.show()

# Profit Margin
region["Profit Margin"].plot(kind="bar")
plt.title("Profit Margin by Region")
plt.xticks(rotation=45)
plt.show()

