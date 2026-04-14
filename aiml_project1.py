import pandas as pd 
data = pd.read_csv("students.csv")

subjects=["maths","science","english"]
data["average"]=data[subjects].mean(axis=1)
data["result"]=data["average"].apply(lambda x: "pass" if x>70 else "fail")

X=data[subjects]
y=data["result"]

from sklearn.model_selection import train_test_split
[X_train,X_test,y_train,y_test]=train_test_split(X,y,test_size=0.2,random_state=42)

from sklearn.preprocessing import StandardScaler
scaler=StandardScaler()
X_train=scaler.fit_transform(X_train)
X_test=scaler.transform(X_test)

from sklearn.linear_model import LogisticRegression
model=LogisticRegression()
model.fit(X_train,y_train)
prediction = model.predict(X_test)

from sklearn.tree import DecisionTreeClassifier

dt_model = DecisionTreeClassifier()
dt_model.fit(X_train, y_train)

dt_pred = dt_model.predict(X_test)

from sklearn.ensemble import RandomForestClassifier

rf_model = RandomForestClassifier()
rf_model.fit(X_train, y_train)

rf_pred = rf_model.predict(X_test)

from sklearn.metrics import accuracy_score,classification_report
print("Accuracy:",accuracy_score(y_test,prediction)*100)
print("Decision Tree:", accuracy_score(y_test, dt_pred)*100)
print("Random Forest:", accuracy_score(y_test, rf_pred)*100)
print("Logistic\n",classification_report(y_test,prediction))
print("Decision Tree\n", classification_report(y_test, dt_pred))
print("Random Forest\n", classification_report(y_test, rf_pred))

new_student=[[85,80,78]]
new_student=scaler.transform(new_student)
result=model.predict(new_student)
print("Pass/Fail:",result)