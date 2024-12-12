import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

# Create dummy F1 dataset with 100 records
data = {
    "Driver": [f"Driver_{i}" for i in range(1, 101)],
    "Team": [f"Team_{np.random.randint(1, 11)}" for _ in range(100)],
    "Race": [f"Race_{np.random.randint(1, 21)}" for _ in range(100)],
    "Position": np.random.randint(1, 21, size=100),
    "Points": [np.random.choice([None, np.random.randint(0, 26)]) for _ in range(100)],
    "Fastest_Lap_Time": [
        np.random.choice([None, round(np.random.uniform(1.0, 1.5), 3)]) for _ in range(100)
    ],
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Export dataset for Excel compatibility
df.to_csv("f1_dataset.csv", index=False)

# 1. Fillna: Fill missing values with the median for numerical columns and "Unknown" for categorical columns
df["Points"] = df["Points"].fillna(df["Points"].median())
df["Fastest_Lap_Time"] = df["Fastest_Lap_Time"].fillna(df["Fastest_Lap_Time"].median())
df["Team"] = df["Team"].fillna("Unknown")

# Print dataset after fillna
print("Dataset after fillna:\n", df.head())

# 2. Dropna: Drop rows with any missing values (shouldn't drop any after fillna)
df_cleaned = df.dropna()

# Print dataset after dropna
print("Dataset after dropna:\n", df_cleaned.head())

# 3. Map: Add a new column indicating if the driver scored points or not
df_cleaned["Scored_Points"] = df_cleaned["Points"].map(lambda x: "Yes" if x > 0 else "No")

# Print dataset after map
print("Dataset after map:\n", df_cleaned.head())

# 4. Normalize: Normalize the Points and Fastest_Lap_Time columns using MinMaxScaler
scaler = MinMaxScaler()
df_cleaned[["Points", "Fastest_Lap_Time"]] = scaler.fit_transform(
    df_cleaned[["Points", "Fastest_Lap_Time"]]
)

# Print dataset after normalization
print("Dataset after normalization:\n", df_cleaned.head())
