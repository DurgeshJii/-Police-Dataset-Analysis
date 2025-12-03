import pandas as pd

# -----------------------------------------------------------
# 1️⃣ Load Dataset
# -----------------------------------------------------------
df = pd.read_csv("police dataset.csv")

print("Dataset Loaded Successfully!")
print(df.head())
print("\nShape:", df.shape)

# -----------------------------------------------------------
# 2️⃣ Remove Column With All Missing Values
# -----------------------------------------------------------
print("\nNull Values Before Cleaning:")
print(df.isnull().sum())

df.drop(columns="country_name", inplace=True)

print("\nColumn 'country_name' removed.")
print(df.sample(4))

# -----------------------------------------------------------
# 3️⃣ For Speeding, were Men or Women stopped more often?
# -----------------------------------------------------------
speeding_counts = df[df["violation"] == "Speeding"]["driver_gender"].value_counts()

print("\nWho was stopped more for Speeding?")
print(speeding_counts)

# -----------------------------------------------------------
# 4️⃣ Does gender affect who gets searched?
# -----------------------------------------------------------
search_by_gender = df.groupby("driver_gender")["search_conducted"].sum()

print("\nSearch Conducted Count by Gender:")
print(search_by_gender)

print("\nSearch Conducted Value Counts:")
print(df["search_conducted"].value_counts())

# -----------------------------------------------------------
# 5️⃣ What is the Mean Stop Duration? (Mapping + Type Casting)
# -----------------------------------------------------------
print("\nStop Duration Value Counts:")
print(df["stop_duration"].value_counts())

duration_mapping = {
    "0-15 Min": 7.5,
    "16-30 Min": 24,
    "30+ Min": 45
}

df["stop_duration"] = df["stop_duration"].map(duration_mapping)

print("\nConverted Stop Duration:")
print(df.head())

mean_duration = df["stop_duration"].mean()
print("\nMean Stop Duration:", mean_duration)

# -----------------------------------------------------------
# 6️⃣ Compare Age Distributions for Each Violation
# -----------------------------------------------------------
age_distribution = df.groupby("violation")["driver_age"].describe()

print("\nAge Distribution for Each Violation:")
print(age_distribution)

# -----------------------------------------------------------
# (Optional) Save cleaned dataset
# -----------------------------------------------------------
df.to_csv("cleaned_police_dataset.csv", index=False)
print("\nCleaned dataset saved as cleaned_police_dataset.csv")
