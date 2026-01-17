import pandas as pd
import matplotlib.pyplot as plt
import os

# -----------------------------
# Load Dataset (Bulletproof Path)
# -----------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(BASE_DIR, "vgsales.csv")

df = pd.read_csv(csv_path)

# -----------------------------
# Data Cleaning
# -----------------------------
df = df.dropna()
df["Year"] = df["Year"].astype(int)

# -----------------------------
# Analysis
# -----------------------------

# Genre Sales
genre_sales = (
    df.groupby("Genre")["Global_Sales"]
    .sum()
    .sort_values(ascending=False)
)

# Platform Sales (Top 10)
platform_sales = (
    df.groupby("Platform")["Global_Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

# Sales Over Time
yearly_sales = (
    df.groupby("Year")["Global_Sales"]
    .sum()
)

# -----------------------------
# Visualization (All Charts Together)
# -----------------------------
fig, axes = plt.subplots(1, 3, figsize=(18, 5))

# 1️⃣ Genre Sales
genre_sales.plot(
    kind="bar",
    ax=axes[0],
    title="Global Video Game Sales by Genre"
)
axes[0].set_xlabel("Genre")
axes[0].set_ylabel("Global Sales (Millions)")

# 2️⃣ Platform Sales
platform_sales.plot(
    kind="bar",
    ax=axes[1],
    title="Top 10 Platforms by Global Sales"
)
axes[1].set_xlabel("Platform")
axes[1].set_ylabel("Global Sales (Millions)")

# 3️⃣ Sales Over Time
yearly_sales.plot(
    ax=axes[2],
    title="Global Video Game Sales Over Time"
)
axes[2].set_xlabel("Year")
axes[2].set_ylabel("Global Sales (Millions)")

plt.tight_layout()
plt.show()
