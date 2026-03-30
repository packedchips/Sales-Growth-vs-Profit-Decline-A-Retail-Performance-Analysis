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

#Prooving it
monthly["Profit Margin"] = monthly["Profit"] / monthly["Sales"]
print(monthly[["Year", "Month", "Profit Margin"]])

#visualize profit margin trend
import matplotlib.pyplot as plt
plt.plot(monthly["Profit Margin"])
plt.title("Profit Margin Trend")
plt.show()
#from this we can see that our profit margin is declining
#this means that there is inefficiency in our pricing discounting or cost structure

#so we can check impact of multiple factors in our data, starting with discount