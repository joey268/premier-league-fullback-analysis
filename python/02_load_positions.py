import sys
import pandas as pd

# Allow the Windows terminal to display UTF-8 characters correctly
sys.stdout.reconfigure(encoding="utf-8")

base_url = "https://raw.githubusercontent.com/Samoilov2004/premier_league_dataset/refs/heads/main/dataset/DATA_CSV/Season_2025/"

clubs = {
    "Bournemouth": "AFC_Bournemouth_989_2025.csv",
    "Arsenal": "Arsenal_FC_11_2025.csv",
    "Aston Villa": "Aston_Villa_405_2025.csv",
    "Brentford": "Brentford_FC_1148_2025.csv",
    "Brighton": "Brighton_and_Hove_Albion_1237_2025.csv",
    "Burnley": "Burnley_FC_1132_2025.csv",
    "Chelsea": "Chelsea_FC_631_2025.csv",
    "Crystal Palace": "Crystal_Palace_873_2025.csv",
    "Everton": "Everton_FC_29_2025.csv",
    "Fulham": "Fulham_FC_931_2025.csv",
    "Leeds United": "Leeds_United_399_2025.csv",
    "Liverpool": "Liverpool_FC_31_2025.csv",
    "Manchester City": "Manchester_City_281_2025.csv",
    "Manchester United": "Manchester_United_985_2025.csv",
    "Newcastle": "Newcastle_United_762_2025.csv",
    "Nottingham Forest": "Nottingham_Forest_703_2025.csv",
    "Sunderland": "Sunderland_AFC_289_2025.csv",
    "Tottenham": "Tottenham_Hotspur_148_2025.csv",
    "West Ham": "West_Ham_United_379_2025.csv",
    "Wolves": "Wolverhampton_Wanderers_543_2025.csv"
}

# -----------------------------
# 1. Load detailed position data
# -----------------------------

club_dfs = []

for club, filename in clubs.items():
    url = base_url + filename

    club_df = pd.read_csv(url)
    club_df["SeasonSquad"] = club

    club_dfs.append(club_df)

combined_df = pd.concat(
    club_dfs,
    ignore_index=True
)

# Keep only full-backs
fullbacks_df = combined_df[
    combined_df["position"].isin(
        ["Left-Back", "Right-Back"]
    )
].copy()

# -----------------------------
# 2. Normalise squad names
# -----------------------------

squad_name_map = {
    "Manchester United": "Manchester Utd",
    "Nottingham Forest": "Nottingham"
}

fullbacks_df["FBrefSquad"] = (
    fullbacks_df["SeasonSquad"]
    .replace(squad_name_map)
)

# -----------------------------
# 3. Normalise known player names
# -----------------------------

name_map = {
    "Andrew Robertson": "Andy Robertson",
    "Ferdi Kadıoğlu": "Ferdi Kadioglu",
    "Josh Acheampong": "Joshua Acheampong"
}

fullbacks_df["FBrefName"] = (
    fullbacks_df["name"]
    .replace(name_map)
)

# -----------------------------
# 4. Load processed FBref data
# -----------------------------

fbref_df = pd.read_csv(
    "data/processed/premier_league_players.csv",
    encoding="utf-8"
)

# -----------------------------
# 5. Merge the two datasets
# -----------------------------

fullback_stats_df = pd.merge(
    fbref_df,
    fullbacks_df,
    left_on=["Player", "Squad"],
    right_on=["FBrefName", "FBrefSquad"],
    how="inner"
)

# -----------------------------
# 6. Calculate percentiles
# -----------------------------

fullback_stats_df["Crs_percentile"] = (
    fullback_stats_df["Crs_per90"]
    .rank(pct=True) * 100
)

fullback_stats_df["Int_percentile"] = (
    fullback_stats_df["Int_per90"]
    .rank(pct=True) * 100
)

fullback_stats_df["TklW_percentile"] = (
    fullback_stats_df["TklW_per90"]
    .rank(pct=True) * 100
)

# -----------------------------
# 7. Add benchmark medians
# -----------------------------

fullback_stats_df["Crs_median"] = (
    fullback_stats_df["Crs_per90"].median()
)

fullback_stats_df["Int_median"] = (
    fullback_stats_df["Int_per90"].median()
)

fullback_stats_df["TklW_median"] = (
    fullback_stats_df["TklW_per90"].median()
)

# -----------------------------
# 8. Keep only Power BI fields
# -----------------------------

powerbi_df = fullback_stats_df[
    [
        "Player",
        "PlayerID",
        "Squad",
        "position",
        "90s",
        "Crs",
        "Int",
        "TklW",
        "Crs_per90",
        "Int_per90",
        "TklW_per90",
        "Crs_percentile",
        "Int_percentile",
        "TklW_percentile",
        "Crs_median",
        "Int_median",
        "TklW_median"
    ]
].copy()

# -----------------------------
# 9. Sort and export
# -----------------------------

powerbi_df = powerbi_df.sort_values(
    by="Crs_percentile",
    ascending=False
)

powerbi_df.to_csv(
    "data/processed/premier_league_fullbacks.csv",
    index=False,
    encoding="utf-8-sig"
)

# -----------------------------
# 10. Create Power BI comparison table
# -----------------------------

comparison_df = pd.DataFrame({
    "Player": powerbi_df["Player"],
    "Squad": powerbi_df["Squad"],
    "Crosses / 90": powerbi_df["Crs_per90"],
    "Interceptions / 90": powerbi_df["Int_per90"],
    "Tackles Won / 90": powerbi_df["TklW_per90"]
})

comparison_df = comparison_df.melt(
    id_vars=["Player", "Squad"],
    var_name="Metric",
    value_name="PlayerValue"
)

median_map = {
    "Crosses / 90": powerbi_df["Crs_per90"].median(),
    "Interceptions / 90": powerbi_df["Int_per90"].median(),
    "Tackles Won / 90": powerbi_df["TklW_per90"].median()
}

comparison_df["FullbackMedian"] = (
    comparison_df["Metric"].map(median_map)
)

comparison_df.to_csv(
    "data/processed/fullback_comparison.csv",
    index=False,
    encoding="utf-8-sig"
)

# -----------------------------
# 11. Quick checks
# -----------------------------

print(
    f"Exported {len(powerbi_df)} qualifying full-backs."
)

print("\nLewis Hall:")
print(
    powerbi_df[
        powerbi_df["Player"] == "Lewis Hall"
    ][
        [
            "Player",
            "Squad",
            "90s",
            "Crs_per90",
            "Crs_percentile",
            "Int_per90",
            "Int_percentile",
            "TklW_per90",
            "TklW_percentile"
        ]
    ].to_string(index=False)
)

print("\nOutput:")
print(
    "data/processed/premier_league_fullbacks.csv"
)