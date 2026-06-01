"""import pandas as pd

# Create a sample DataFrame with an imbalanced target
data = {
    "feature1": [1, 2, 3, 4, 5, 6, 7],
    "target":   ["A", "A", "A", "A", "B", "B", "B"]
}
df = pd.DataFrame(data)

# Count original class distribution
print("Original class distribution:")
print(df["target"].value_counts())

# Oversample minority class "B" to match majority class "A"
majority_count = df["target"].value_counts().max()
minority_class = df["target"].value_counts().idxmin()

# Get all minority class rows
minority_rows = df[df["target"] == minority_class]

# Calculate how many samples to add
samples_to_add = majority_count - len(minority_rows)

# Sample with replacement from minority class
oversampled_minority = minority_rows.sample(n=samples_to_add, replace=True, random_state=42)

# Concatenate original data with new samples
df_oversampled = pd.concat([df, oversampled_minority], ignore_index=True)

# Show new class distribution
print("\nClass distribution after oversampling:")
print(df_oversampled["target"].value_counts())
"""

import pandas as pd

def oversample_minority(df, target_column):
    # Count original class distribution
    # print("Original class distribution:")
    # print(df["target"].value_counts())

    # Oversample minority class "B" to match majority class "A"
    majority_count = df[target_column].value_counts().max()
    minority_class = df[target_column].value_counts().idxmin()

    # Get all minority class rows
    minority_rows = df[df[target_column] == minority_class]

    # Calculate how many samples to add
    samples_to_add = majority_count - len(minority_rows)

    # Sample with replacement from minority class
    newsample_minority = minority_rows.sample(n=samples_to_add, replace=True, random_state=42)

    # Concatenate original data with new samples
    return pd.concat([df, newsample_minority], ignore_index=True)
    
data = {
    "feature1": [1, 2, 3, 4, 5, 6],
    "target": ["A", "A", "A", "B", "B", "B"]
}

df = pd.DataFrame(data)
df = df.iloc[:-1]       # reassigns df to a slice of itself that includes every row except the very last one

balanced_df = oversample_minority(df, "target")

result_shape = balanced_df.shape
result_counts = balanced_df["target"].value_counts()
print(result_shape)
print(result_counts)
