import pandas as pd
import numpy as np

data = {
    "Player": ["Hardik Pandya", "KL Rahul", "Andre Russel", "Jasprit Bumrah", "Virat Kohli", "Rohit Sharma"],
    "Team": ["Mumbai Indians", "Kings Eleven", "Kolkata Knight Riders", "Mumbai Indians", "RCB", "Mumbai Indians"],
    "Category": ["Batsman", "Batsman", "Batsman", "Bowler", "Batsman", "Batsman"],
    "BidPrice": [13, 12, np.nan, 10, 17, np.nan],
    "Runs": [1000, 2400, 900, 200, 3600, 3700]
}

df = pd.DataFrame(data)

print("First 2 rows:")
print(df.head(2))

print("\nLast 3 rows:")
print(df.tail(3))

print("\nNull values:")
print(df.isnull())

df["BidPrice"] = df["BidPrice"].fillna(df["BidPrice"].mean())
print("\nAfter replacing nulls with mean:")
print(df)

print("\nMost expensive player:")
print(df.loc[df["BidPrice"].idxmax(), "Player"])

print("\nTotal players per team:")
print(df.groupby("Team")["Player"].count())
