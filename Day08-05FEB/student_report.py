import pandas as pd
import matplotlib.pyplot as plt


data = {
    "Name": ["Aarav", "Diya", "Rohan", "Meera", "Kabir"],
    "Age": [18, None, 17, 18, None],
    "Marks": [85, 92, None, 68, 74],
    "Class": ["12A", "12A", "12B", "12A", "12B"],
    "City": [" Delhi ", "mumbai", "Bangalore ", " delhi", "MUMBAI "]
}

df = pd.DataFrame(data)
df.to_csv("student_report.csv", index=False)
print("CSV file created: student_report.csv\n")


print("Missing values:")
print(df.isnull().sum(), "\n")


df["Age"].fillna(df["Age"].mean(), inplace=True)
df["Marks"].fillna(df["Marks"].mean(), inplace=True)


df["City"] = df["City"].str.strip().str.title()

print("Cleaned Data:")
print(df, "\n")


average_marks = df["Marks"].mean()
print("Average Marks:", average_marks)


top_student = df.loc[df["Marks"].idxmax()]
print("\nTop Scoring Student:")
print(top_student)


below_70 = df[df["Marks"] < 70]
print("\nStudents scoring below 70:")
print(below_70)


plt.figure()
plt.bar(df["Name"], df["Marks"])
plt.xlabel("Student Name")
plt.ylabel("Marks")
plt.title("Marks vs Students")
plt.show()