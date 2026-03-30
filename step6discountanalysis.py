import pandas as pd

df = pd.read_csv("sales.csv")

# Convert date
df["Order Date"] = pd.to_datetime(df["Order Date"], format="mixed", dayfirst=True)

# Create new columns
df["Month"] = df["Order Date"].dt.month
df["Year"] = df["Order Date"].dt.year


# Discount Analysis
discount_analysis = df.groupby("Discount")[["Sales", "Profit"]].mean().reset_index()
# make a visualization
import matplotlib.pyplot as plt
import numpy as np
x = discount_analysis["Discount"]
y = discount_analysis["Profit"]
plt.figure()
plt.scatter(x,y)

z = np.polyfit(x, y, 1)
p = np.poly1d(z)
plt.plot(x, p(x))
plt.title("Discount vs Profit")
plt.xlabel("Discount")
plt.ylabel("AVG Profit")
plt.show()