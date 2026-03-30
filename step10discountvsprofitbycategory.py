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
    x = analysis["Discount"]
    y = analysis["Profit"]
    plt.figure()
    plt.scatter(x, y)
    
    # Trend line
    z = np.polyfit(x, y, 1)
    p = np.poly1d(z)
    plt.plot(x, p(x))
    plt.title(f"Discount vs Profit ({cat})")
    plt.xlabel("Discount")
    plt.ylabel("Avg Profit")
    plt.show()

# this analysis we can see that the discount sensitivity varies
# snacks show strongest negative relation
# poultry stays flat which means that discounting is not impacting profit 
# bakery shows a positive relation which means that discounting is helping to boost profit

# Negative slope → discount hurting profit
# Near zero → no effect
# Positive → good discount which boosts profit