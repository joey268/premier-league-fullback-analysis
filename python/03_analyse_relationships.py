import pandas as pd
import numpy as np

df = pd.read_csv("data/processed/premier_league_fullbacks.csv")

print(df[[
    "Player",
    "Crs_per90",
    "Int_per90",
    "TklW_per90"
]].head())

print(f"\nNumber of full-backs: {len(df)}")

# Calculate correlations

cross_tackle_corr = df["Crs_per90"].corr(df["TklW_per90"])
cross_interception_corr = df["Crs_per90"].corr(df["Int_per90"])

print("\nCorrelations:")
print(f"Crosses vs Tackles Won: {cross_tackle_corr:.3f}")
print(f"Crosses vs Interceptions: {cross_interception_corr:.3f}")

from scipy.stats import pearsonr

tackle_r, tackle_p = pearsonr(
    df["Crs_per90"],
    df["TklW_per90"]
)

interception_r, interception_p = pearsonr(
    df["Crs_per90"],
    df["Int_per90"]
)

print("\nStatistical significance:")

print(
    f"Crosses vs Tackles Won: "
    f"r = {tackle_r:.3f}, p = {tackle_p:.3f}"
)

print(
    f"Crosses vs Interceptions: "
    f"r = {interception_r:.3f}, p = {interception_p:.3f}"
)

import matplotlib.pyplot as plt

plt.scatter(df["Crs_per90"], df["TklW_per90"])

x = df["Crs_per90"]
y = df["TklW_per90"]

m, b = np.polyfit(x, y, 1)
plt.plot(x, m * x + b)

plt.xlabel("Crosses per 90")
plt.ylabel("Tackles Won per 90")
plt.title("Crossing vs Tackles Won – Premier League Full-Backs")
plt.show()
plt.scatter(df["Crs_per90"], df["Int_per90"])

x = df["Crs_per90"]
y = df["Int_per90"]

m, b = np.polyfit(x, y, 1)
plt.plot(x, m * x + b)

plt.xlabel("Crosses per 90")
plt.ylabel("Interceptions per 90")
plt.title("Crossing vs Interceptions – Premier League Full-Backs")
plt.show()

from scipy.stats import spearmanr

tackle_spearman_r, tackle_spearman_p = spearmanr(
    df["Crs_per90"],
    df["TklW_per90"]
)

interception_spearman_r, interception_spearman_p = spearmanr(
    df["Crs_per90"],
    df["Int_per90"]
)

print("\nSpearman correlations:")

print(
    f"Crosses vs Tackles Won: "
    f"r = {tackle_spearman_r:.3f}, p = {tackle_spearman_p:.3f}"
)

print(
    f"Crosses vs Interceptions: "
    f"r = {interception_spearman_r:.3f}, p = {interception_spearman_p:.3f}"
)