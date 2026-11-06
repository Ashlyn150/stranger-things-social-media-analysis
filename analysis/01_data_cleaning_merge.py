# ============================================================
#  Stranger Things — Data Cleaning & Merging
#  IMDb + Reddit -> combined_data.csv
#
#  Install dependencies: pip install pandas openpyxl
# ============================================================

import pandas as pd

# ── Season time windows (based on premiere dates) ────────────
SEASON_WINDOWS = [
    ("Season 1", "2016-07-15", "2017-10-26"),
    ("Season 2", "2017-10-27", "2019-07-03"),
    ("Season 3", "2019-07-04", "2022-05-26"),
    ("Season 4", "2022-05-27", "2025-11-25"),
    ("Season 5", "2025-11-26", "2099-12-31"),
]

def assign_season(date):
    for season, start, end in SEASON_WINDOWS:
        if pd.Timestamp(start) <= date <= pd.Timestamp(end):
            return season
    return "Unknown"


# ============================================================
#  Step 1: IMDb Data Cleaning
# ============================================================
print("=" * 60)
print("Processing IMDb data...")
print("=" * 60)

df_imdb = pd.read_csv("stranger_things_reviews.csv")
print(f"Raw row count: {len(df_imdb)}")

# Drop unnecessary columns
df_imdb = df_imdb.drop(columns=["no"])

# Standardise date format
df_imdb["date"] = pd.to_datetime(df_imdb["date"], format="mixed")

# Assign season label by date
df_imdb["season"] = df_imdb["date"].apply(assign_season)
print(f"\nSeason distribution (IMDb):")
print(df_imdb["season"].value_counts().sort_index())

# Drop rows where content is missing
before = len(df_imdb)
df_imdb = df_imdb.dropna(subset=["content"])
print(f"\nRows removed (empty content): {before - len(df_imdb)}")

# Filter out very short text
before = len(df_imdb)
df_imdb = df_imdb[df_imdb["content"].str.len() >= 20]
print(f"Rows removed (text < 20 chars): {before - len(df_imdb)}")

# Remove duplicates
before = len(df_imdb)
df_imdb = df_imdb.drop_duplicates(subset=["author", "content"])
print(f"Rows removed (duplicates): {before - len(df_imdb)}")

# Keep missing ratings as NaN
print(f"Missing ratings: {df_imdb['rating'].isna().sum()} rows (kept as NaN)")

# Convert helpful votes to numeric
df_imdb["helpful"]     = pd.to_numeric(df_imdb["helpful"],     errors="coerce").fillna(0).astype(int)
df_imdb["not_helpful"] = pd.to_numeric(df_imdb["not_helpful"], errors="coerce").fillna(0).astype(int)

# Calculate text_len
df_imdb["text_len"] = df_imdb["content"].str.len()

# Rename columns and add source label
df_imdb = df_imdb.rename(columns={
    "content":     "text",
    "helpful":     "helpful_votes",
    "not_helpful": "not_helpful_votes",
})
df_imdb["source"] = "IMDb"

# Select and order columns
imdb_clean = df_imdb[[
    "source", "season", "date", "author", "title",
    "text", "text_len",
    "rating",
    "helpful_votes",
    "not_helpful_votes",
]].copy()

# Fill Reddit-only columns with NaN
imdb_clean["score"]        = pd.NA
imdb_clean["num_comments"] = pd.NA
imdb_clean["flair"]        = pd.NA

print(f"\nIMDb cleaned row count: {len(imdb_clean)}")


# ============================================================
#  Step 2: Reddit Data Cleaning
# ============================================================
print("\n" + "=" * 60)
print("Processing Reddit data...")
print("=" * 60)

df_reddit = pd.read_csv("Reddit_stranger_things_cleaned_data.csv")
print(f"Raw row count: {len(df_reddit)}")

# Standardise date format
df_reddit["date"] = pd.to_datetime(df_reddit["date"])

# Calculate text_len
df_reddit["text_len"] = df_reddit["text"].str.len()

# Basic stats
print(f"Empty text: {df_reddit['text'].isna().sum()} rows")
print(f"Very short text (< 20 chars): {(df_reddit['text_len'] < 20).sum()} rows")
print(f"Duplicate posts (by url): {df_reddit.duplicated(subset=['url']).sum()} rows")
print(f"Deleted users: {(df_reddit['author'] == '[deleted]').sum()} rows")

# Drop unnecessary columns
df_reddit = df_reddit.drop(columns=["created_utc", "url"])

# Fill missing flair
df_reddit["flair"] = df_reddit["flair"].fillna("Unflaired")

# Add source label
df_reddit["source"] = "Reddit"

# Select and order columns
reddit_clean = df_reddit[[
    "source", "season", "date", "author", "title",
    "text", "text_len",
    "score",
    "num_comments",
    "flair",
]].copy()

# Fill IMDb-only columns with NaN
reddit_clean["rating"]            = pd.NA
reddit_clean["helpful_votes"]     = pd.NA
reddit_clean["not_helpful_votes"] = pd.NA

print(f"\nReddit cleaned row count: {len(reddit_clean)}")


# ============================================================
#  Step 3: Merge
# ============================================================
print("\n" + "=" * 60)
print("Merging datasets...")
print("=" * 60)

df_all = pd.concat([imdb_clean, reddit_clean], ignore_index=True)
df_all = df_all.sort_values(["season", "date"]).reset_index(drop=True)

# Final column order
final_cols = [
    "source", "season", "date", "author", "title",
    "text", "text_len",
    "rating", "helpful_votes", "not_helpful_votes",
    "score", "num_comments", "flair",
]
df_all = df_all[final_cols]

print(f"Total rows after merge: {len(df_all)}")
print(f"\nRows by source:")
print(df_all["source"].value_counts())
print(f"\nRows by season:")
print(df_all["season"].value_counts().sort_index())
print(f"\nMissing values:")
print(df_all.isnull().sum())


# ============================================================
#  Step 4: Export
# ============================================================
print("\n" + "=" * 60)
print("Saving files...")
print("=" * 60)

df_all.to_csv("combined_data.csv", index=False)
print("combined_data.csv saved")

with pd.ExcelWriter("combined_data.xlsx", engine="openpyxl") as writer:
    df_all.to_excel(writer, sheet_name="All Data", index=False)
    df_all[df_all["source"] == "IMDb"].to_excel(writer, sheet_name="IMDb", index=False)
    df_all[df_all["source"] == "Reddit"].to_excel(writer, sheet_name="Reddit", index=False)
print("combined_data.xlsx saved (3 sheets: All Data / IMDb / Reddit)")

print("\nDone!")
print(f"Final dataset: {len(df_all)} rows x {len(df_all.columns)} columns")
