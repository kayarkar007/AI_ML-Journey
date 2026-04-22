# import pandas as pd 
# data= pd.read_csv("students.csv")
# print(data.head())
# print(data.info())
# print(data.describe())

# subjects=["maths","science","english"]
# data["Average"]=data[subjects].mean(axis=1)
# print(data["Average"])
# Topper_student=data["Average"].idxmax()
# print(data["name"][Topper_student])
# data["pass_fail"]=data["Average"].apply(lambda x:"pass" if x>70 else "fail")
# print(data["pass_fail"].value_counts())

# print("Topper of the class:")
# print(data[["name","Average"]].loc[Topper_student])
# print("No of students passed:")

# print(data["pass_fail"].value_counts()["pass"])

# print("No of students failed:")

# print(data["pass_fail"].value_counts()["fail"])

# data["result"]=data["Average"].apply(lambda x:"1" if x>70 else "0")

# X=data[subjects]
# y=data["result"]

# from sklearn.model_selection import train_test_split
# X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)

# # from sklearn.preprocessing import StandardScaler
# # scaler=StandardScaler()
# # X_train=scaler.fit_transform(X_train)
# # X_test=scaler.transform(X_test)


# from sklearn.linear_model import LogisticRegression
# from sklearn.tree import DecisionTreeClassifier
# from sklearn.ensemble import RandomForestClassifier
# model={
#     "Logistic": LogisticRegression(),
#     "Decision Tree": DecisionTreeClassifier(),
#     "Random Forest": RandomForestClassifier(n_estimators=50)
# }

# from sklearn.metrics import accuracy_score  
# for name, model in model.items():
#     model.fit(X_train, y_train)
#     y_pred = model.predict(X_test)
#     print(name, "Accuracy:", accuracy_score(y_test, y_pred)*100)

# new_student=[[10,10,18]]
# result=model.predict(new_student)
# print(result)



import pandas as pd

# Load data
data = pd.read_csv("students.csv")

subjects=["maths","science","english"]
# Target = average marks
data["average"] = data[subjects].mean(axis=1)

# X and y
X = data[subjects]
y = data["average"]

# Split
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Scaling
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Regression model
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

# Evaluation
from sklearn.metrics import mean_absolute_error, r2_score

print("MAE:", mean_absolute_error(y_test, y_pred))
print("R2 Score:", r2_score(y_test, y_pred))

# Test new student
new_student = [[85, 80, 78]]
new_student_scaled = scaler.transform(new_student)


predicted_average = model.predict(new_student_scaled)
print("Predicted Average:", predicted_average[0])