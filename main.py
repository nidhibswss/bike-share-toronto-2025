import pandas as pd

files = [
    "bikeshare_2025_01.csv", "bikeshare_2025_02.csv", "bikeshare_2025_03.csv",
    "bikeshare_2025_04.csv", "bikeshare_2025_05.csv", "bikeshare_2025_06.csv",
    "bikeshare_2025_07.csv", "bikeshare_2025_08.csv", "bikeshare_2025_09.csv",
    "bikeshare_2025_10.csv", "bikeshare_2025_11.csv", "bikeshare_2025_12.csv"
]

df_list = []

for file in files:
    print(f"Reading file: {file}")
    monthly_df = pd.read_csv(
        file,
        encoding="latin1",
        on_bad_lines="skip",
        low_memory=False
    )
    df_list.append(monthly_df)

df = pd.concat(df_list, ignore_index=True)

print("\nFINAL DATA SHAPE:", df.shape)

# ------------------- DATA PREPROCESSING -------------------

# Clean column names
df.columns = df.columns.str.lower().str.strip()

# Check missing values
print("\nMissing values:")
print(df.isnull().sum())

# Convert time columns
df['start_time'] = pd.to_datetime(df['start_time'])
df['end_time'] = pd.to_datetime(df['end_time'])

# Create new features
df['month'] = df['start_time'].dt.month
df['hour'] = df['start_time'].dt.hour
df['day_of_week'] = df['start_time'].dt.day_name()
df['month_name'] = df['start_time'].dt.month_name()

print("\nDATA SHAPE AFTER PREPROCESSING:", df.shape)
print(df.head())

# Save cleaned dataset
df.to_csv("cleaned_bikeshare_2025.csv", index=False)
print("\nSaved cleaned_bikeshare_2025.csv")