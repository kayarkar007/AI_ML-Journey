import pandas as pd
data=pd.read_csv("loan_approval_dataset.csv")
print(data.head())
print(data.info())
data.columns = data.columns.str.strip()
print(data.head())

data.columns = data.columns.str.strip()
data["education"]=data["education"].str.strip()
data["self_employed"]=data["self_employed"].str.strip() 
data["loan_status"]=data["loan_status"].str.strip()
data["education"]=data["education"].map({"Graduate":1,"Not Graduate":0})
data["self_employed"]=data["self_employed"].map({"Yes":1,"No":0})
data["loan_status"]=data["loan_status"].map({"Approved":1,"Rejected":0})
print(data.head())


data=data.drop("loan_id",axis=1)
X=data.drop("loan_status",axis=1)
y=data["loan_status"]
print(X.head())
print(y.head())

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

y_pred=model.predict(X_test)
# print(y_pred)

from sklearn.metrics import accuracy_score, classification_report

print("Accuracy:", accuracy_score(y_test, y_pred)*100)
print(classification_report(y_test, y_pred))


import pandas as pd

importance = model.feature_importances_

feature_names = X.columns

df = pd.DataFrame({
    "Feature": feature_names,
    "Importance": importance
})

print(df.sort_values(by="Importance", ascending=False))

data["loan_income_ratio"] = data["loan_amount"] / (data["income_annum"] + 1)

data["total_assets"] = (
    data["residential_assets_value"] +
    data["commercial_assets_value"] +
    data["luxury_assets_value"] +
    data["bank_asset_value"]
)

data["loan_assets_ratio"] = data["loan_amount"] / (data["total_assets"] + 1)
X = data.drop("loan_status", axis=1)
y = data["loan_status"]

from sklearn.linear_model import LogisticRegression

lr_model = LogisticRegression()
lr_model.fit(X_train, y_train)

lr_pred = lr_model.predict(X_test)

print("Logistic Accuracy:", accuracy_score(y_test, lr_pred)*100)