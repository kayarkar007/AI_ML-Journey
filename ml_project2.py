import pandas as pd

# Load data
data = pd.read_csv("students.csv")

# Clean column names (important in real world)
data.columns = data.columns.str.strip()

# Subjects list
subjects = ["maths", "science", "english"]

# 1. Average marks per student
data["average"] = data[subjects].mean(axis=1)

# 2. Class average
class_average = data["average"].mean()

# 3. Topper (highest average)
topper = data.loc[data["average"].idxmax()]

# 4. Top 3 students
top3 = data.sort_values(by="average", ascending=False).head(3)

# 5. Fail students (avg < 70)
fail_students = data[data["average"] < 70]

# 6. Pass students
pass_students = data[data["average"] >= 70]

# 7. Subject-wise topper
subject_toppers = {}
for subject in subjects:
    idx = data[subject].idxmax()
    subject_toppers[subject] = data.loc[idx]["name"]

# ---------------- OUTPUT ---------------- #

print("📊 Class Average:", round(class_average, 2))

print("\n🏆 Topper:")
print(topper["name"], "-", round(topper["average"], 2))

print("\n🥇 Top 3 Students:")
print(top3[["name", "average"]])

print("\n❌ Fail Students:")
print(fail_students[["name", "average"]])

print("\n✅ Pass Students:")
print(pass_students[["name", "average"]])

print("\n📚 Subject-wise Toppers:")
for subject, name in subject_toppers.items():
    print(f"{subject.capitalize()}: {name}")