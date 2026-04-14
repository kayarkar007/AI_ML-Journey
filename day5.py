# import pandas as pd

# # Load data
# data = pd.read_csv("students.csv")

# # Feature engineering
# data["average"] = (data["maths"] + data["science"] + data["english"]) / 3
# data["result"] = data["average"].apply(lambda x: 1 if x > 70 else 0)
# data["rounded_average"]= round(data["average"])
# data["Pass/Fail"]= data["result"].apply(lambda x: "Pass" if x==1 else "Fail")

# # Define features and target
# X = data[["maths", "science", "english"]]
# y = data["result"]

# # Top 3 students
# top_students = data.sort_values(by="average", ascending=False).head(3)
# print("Top 3 students:")
# print(top_students[["name", "rounded_average"]])

# #Failed_Students
# failed_students= data[data["Pass/Fail"]=="Fail"]
# print("Failed Students:")
# print(failed_students["name"])

# #Pass_Students
# Pass_students= data[data["Pass/Fail"]=="Pass"]
# print(Pass_students)

# #Average of the class
# Averageofclass = data["average"].mean()
# print(round(Averageofclass))

# #Subject wise topper 
# subjects = ["maths", "science", "english"]

# for subject in subjects:
#     topper = data.sort_values(by=subject, ascending=False).head(1)
#     print(f"{subject.capitalize()} Topper:")
#     print(topper[["name", subject]])

# # Scaling
# from sklearn.preprocessing import StandardScaler
# scaler = StandardScaler()
# X_scaled = scaler.fit_transform(X)

# # Train-test split
# from sklearn.model_selection import train_test_split
# X_train, X_test, y_train, y_test = train_test_split(
#     X_scaled, y, test_size=0.2, random_state=42
# )

# # Model training
# from sklearn.linear_model import LogisticRegression
# model = LogisticRegression()
# model.fit(X_train, y_train)

# # Prediction
# predictions = model.predict(X_test)

# # Evaluation
# from sklearn.metrics import accuracy_score
# print("Accuracy:", round(accuracy_score(y_test, predictions)*100))

# # top 5 students by average
# top_5= data.sort_values(by="average",ascending=False).head(5)
# print(top_5[["name","average"]])

# #Lowest 5 students
# lowest_5= data.sort_values(by="average",ascending=True).head(5)
# print(lowest_5[["name","average"]])

# #Average marks per subject
# avg=0
# for subject in subjects:
#     avg = round(data[subject].mean())
#     print(f"{subject} average:", avg)

# # students with maths >90;
# top_math_students=data[data["maths"]>90]
# print(top_math_students["name"])
# print("Total students with maths > 90:", len(top_math_students))


# load data 

import pandas as pd 
data = pd.read_csv("students.csv")
print(data)

