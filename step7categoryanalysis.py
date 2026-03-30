import pandas as pd

df = pd.read_csv("sales.csv")

# Convert date
df["Order Date"] = pd.to_datetime(df["Order Date"], format="mixed", dayfirst=True)

# Create new columns
df["Month"] = df["Order Date"].dt.month
df["Year"] = df["Order Date"].dt.year

import matplotlib.pyplot as plt
category = df.groupby("Category")[["Sales", "Profit"]].sum()
category.plot(kind="bar")
plt.title("Sales vs Profit by category")
plt.xlabel("category")
plt.xticks(rotation=45)
plt.show()