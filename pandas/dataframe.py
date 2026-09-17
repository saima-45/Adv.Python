
import pandas as pd

# Create DataFrame
data = {
    "Name": ["Amit", "Neha", "Rahul", "Priya", "Kiran"],
    "Age": [20, 21, 19, 22, 20],
    "City": ["Ahmedabad", "Vadodara", "Surat", "Rajkot", "Ahmedabad"],
    "Marks": [75, 82, 68, 91, 79]
}

df = pd.DataFrame(data)

# Display DataFrame
print("DataFrame:")
print(df)

# Column names
print("\nColumn names:")
print(df.columns)

# Index
print("\nIndex:")
print(df.index)

# Data types
print("\nData types:")
print(df.dtypes)

# Selecting columns
print("\nName column:")
print(df["Name"])

print("\nMarks column:")
print(df["Marks"])

print("\nName and City:")
print(df[["Name", "City"]])

print("\nName, Age and Marks:")
print(df[["Name", "Age", "Marks"]])

# Selecting rows
print("\nFirst row:")
print(df.iloc[0])

print("\nThird row:")
print(df.iloc[2])

print("\nFirst three rows:")
print(df.iloc[:3])

print("\nLast two rows:")
print(df.tail(2))

print("\nFirst 3 rows and first 2 columns:")
print(df.iloc[:3, :2])

print("\nRows 2-4 and Name and Marks:")
print(df.iloc[1:4][["Name", "Marks"]])

print("\nName and Marks of first 3 students:")
print(df.loc[:2, ["Name", "Marks"]])

# DataFrame information
print("\nNumber of rows:", len(df))
print("Number of columns:", len(df.columns))
print("Shape:", df.shape)
print("Columns:", df.columns)
print("Data types:")
print(df.dtypes)

print("\nStatistical information:")
print(df.describe())

# Add Result
df["Result"] = df["Marks"].apply(
    lambda x: "Pass" if x >= 50 else "Fail"
)

# Add Percentage
df["Percentage"] = df["Marks"] / 100 * 100

print("\nUpdated DataFrame:")
print(df)

# Filtering
print("\nMarks greater than 80:")
print(df[df["Marks"] > 80])

print("\nStudents from Vadodara:")
print(df[df["City"] == "Vadodara"])

print("\nMarks > 75 and Age <= 21:")
print(df[(df["Marks"] > 75) & (df["Age"] <= 21)])

# Sorting
print("\nAscending order:")
print(df.sort_values(by="Marks", ascending=True))

print("\nDescending order:")
print(df.sort_values(by="Marks", ascending=False))

# Calculations
print("\nAverage marks:", df["Marks"].mean())
print("Highest marks:", df["Marks"].max())
print("Lowest marks:", df["Marks"].min())

print("\nStudent with highest marks:")
print(df.loc[df["Marks"].idxmax()])

print("\nStudent with lowest marks:")
print(df.loc[df["Marks"].idxmin()])

print("\nTotal number of students:", len(df))

# City count
print("\nStudents in each city:")
print(df["City"].value_counts())

# Missing values
print("\nMissing values:")
print(df.isnull().sum())