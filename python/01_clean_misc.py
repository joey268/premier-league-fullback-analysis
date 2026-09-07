import pandas as pd

# Load the raw FBref data
df = pd.read_csv(
    "data/raw/premier_league_misc.csv",
    encoding="utf-8"
)

# Keep only the columns we need
clean_df = df[
    ["Player", "Pos", "Squad", "90s", "Crs", "Int", "TklW", "-9999"]
].copy()

clean_df.rename(
    columns={"-9999": "PlayerID"},
    inplace=True
)

# Calculate statistics per 90 minutes
clean_df["Crs_per90"] = clean_df["Crs"] / clean_df["90s"]
clean_df["Int_per90"] = clean_df["Int"] / clean_df["90s"]
clean_df["TklW_per90"] = clean_df["TklW"] / clean_df["90s"]

# Keep players with at least 450 minutes
qualified_players_df = clean_df[
    clean_df["90s"] >= 5
]

qualified_players_df.to_csv(
    "data/processed/premier_league_players.csv",
    index=False
)