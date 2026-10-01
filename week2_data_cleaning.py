import pandas as pd

# Load dataset
df = pd.read_csv("logistics_orders.csv")

# Step 2: Data Quality Check

print("Dataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns.tolist())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

print("\nData Types:")
print(df.dtypes)

print("\nBasic Statistics:")
print(df.describe())

# Step 3: Missing Values and Duplicate Check

print("\n--- Step 3: Missing Values and Duplicates ---")

missing_values = df.isnull().sum()
duplicate_rows = df.duplicated().sum()

print("\nMissing Values:")
print(missing_values)

print("\nTotal Missing Values:")
print(missing_values.sum())

print("\nTotal Duplicate Rows:")
print(duplicate_rows)

# Step 4: Outlier Detection using IQR

print("\n--- Step 4: Outlier Detection ---")

numeric_columns = df.select_dtypes(include="number").columns

for column in numeric_columns:
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1

    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    outliers = df[
        (df[column] < lower_bound) |
        (df[column] > upper_bound)
    ]

    print(f"\n{column}: {len(outliers)} outliers")

    # Step 5: Data Cleaning and Preprocessing

print("\n--- Step 5: Data Cleaning and Preprocessing ---")

# Remove duplicate rows
df = df.drop_duplicates()

# Handle missing values
numeric_columns = df.select_dtypes(include="number").columns

for column in numeric_columns:
    df[column] = df[column].fillna(df[column].median())

# Remove extra spaces from text columns
text_columns = df.select_dtypes(include="object").columns

for column in text_columns:
    df[column] = df[column].str.strip()

# Save cleaned dataset
df.to_csv("logistics_orders_cleaned.csv", index=False)

print("\nCleaned Dataset Shape:")
print(df.shape)

print("\nCleaned dataset saved as: logistics_orders_cleaned.csv")

# Step 6: Data Normalization / Standardization

from sklearn.preprocessing import StandardScaler

print("\n--- Step 6: Data Standardization ---")

# Select numerical columns
numeric_columns = df.select_dtypes(include="number").columns

# Standardize numerical data
scaler = StandardScaler()
df_scaled = df.copy()

df_scaled[numeric_columns] = scaler.fit_transform(df[numeric_columns])

# Save standardized dataset
df_scaled.to_csv("logistics_orders_standardized.csv", index=False)

print("\nStandardized Dataset Shape:")
print(df_scaled.shape)

print("\nStandardized dataset saved as: logistics_orders_standardized.csv")

# Step 7: Final Data Quality Verification

print("\n--- Step 7: Final Data Quality Verification ---")

print("\nFinal Dataset Shape:")
print(df.shape)

print("\nFinal Missing Values:")
print(df.isnull().sum().sum())

print("\nFinal Duplicate Rows:")
print(df.duplicated().sum())

print("\nFinal Column Names:")
print(df.columns.tolist())