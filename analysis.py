import pandas as pd
import matplotlib.pyplot as plt

# Read CSV file
df = pd.read_csv("students.csv")

# Display dataset
print("===== STUDENT DATASET =====")
print(df)

# Display information about dataset
print("\n===== DATASET INFORMATION =====")
df.info()

# Display statistical summary
print("\n===== STATISTICAL SUMMARY =====")
print(df.describe())
# Calculate total marks
df["Total"] = df["Math"] + df["Science"] + df["English"]

print("\n===== DATASET WITH TOTAL MARKS =====")
print(df)
# Calculate average marks
df["Average"] = df["Total"] / 3

print("\n===== DATASET WITH AVERAGE =====")
print(df)
# Determine pass or fail
df["Result"] = df["Average"].apply(lambda x: "Pass" if x >= 40 else "Fail")

print("\n===== FINAL DATASET =====")
print(df)
# Find the topper
topper = df.loc[df["Average"].idxmax()]

print("\n===== TOPPER =====")
print(topper)
print("\n===== SUBJECT-WISE AVERAGE =====")

print("Math Average:", df["Math"].mean())
print("Science Average:", df["Science"].mean())
print("English Average:", df["English"].mean())
print("\n===== HIGHEST MARKS =====")

print("Highest Math Marks:", df["Math"].max())
print("Highest Science Marks:", df["Science"].max())
print("Highest English Marks:", df["English"].max())
print("\n===== LOWEST MARKS =====")

print("Lowest Math Marks:", df["Math"].min())
print("Lowest Science Marks:", df["Science"].min())
print("Lowest English Marks:", df["English"].min())
# Save updated data to a new CSV file
df.to_csv("student_report.csv", index=False)

print("\nStudent report saved successfully as 'student_report.csv'")
# Average marks of each subject
subjects = ["Math", "Science", "English"]

average_marks = [
    df["Math"].mean(),
    df["Science"].mean(),
    df["English"].mean()
]

plt.figure(figsize=(6,4))
plt.bar(subjects, average_marks)

plt.title("Average Marks by Subject")
plt.xlabel("Subjects")
plt.ylabel("Average Marks")

plt.show()

# Gender Distribution
gender = df["Gender"].value_counts()

plt.figure(figsize=(5,5))

plt.pie(
    gender,
    labels=gender.index,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Gender Distribution")

plt.show()

# Pass vs Fail
result = df["Result"].value_counts()

plt.figure(figsize=(5,4))

plt.bar(result.index, result.values)

plt.title("Pass vs Fail")
plt.xlabel("Result")
plt.ylabel("Number of Students")

plt.show()

