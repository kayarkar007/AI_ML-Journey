import pandas as pd
data = pd.read_csv("students.csv")
print(data.info())
print(data.describe())
subjects=["maths","science","english"];
data["average"]=data[subjects].mean(axis=1)
print("average:",data["average"])

topper=data.sort_values(by="average",ascending=False);
print("\nTopper")
print(topper[["name","average"]].head(1))
fail_students = data[data["average"]<70]
print("\nFail Students: ")

print(fail_students[["name","average"]].sort_values(by="average",ascending=True))