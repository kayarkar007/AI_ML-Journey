#Load Data
import pandas as pd 
data=pd.read_csv("Telco-Customer-Churn.csv")

#Check and undserstand data
print(data.shape)
print(data.info())
print(data.describe())
print(data.columns)
data.columns=data.columns.str.strip()
print(data.isnull().sum())

#Data featuring

data["TotalCharges"]=pd.to_numeric(data["TotalCharges"],errors="coerce")
data["TotalCharges"]=data["TotalCharges"].fillna(0)
data=data.dropna()
print(data.info())


for col in data.select_dtypes(include="object"):

    data[col] = data[col].astype(str).str.strip()


print(data.info())

data["AverageCharges"]=data["TotalCharges"]/data["tenure"].replace(0,1)

print(data["AverageCharges"].head())
print(data.head())

data["HighValueCustomer"]=(data["AverageCharges"]>70).astype(int)
data["Churn"]=data["Churn"].map({"Yes":1,"No":0})
print(data.head())

X=data.drop(columns=["customerID","Churn"])
y=data["Churn"]

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)

from sklearn.preprocessing import StandardScaler
scaler=StandardScaler()
X_train=scaler.fit_transform(X_train)
X_test=scaler.transform(X_test)

from sklearn.linear_model import LogisticRegression
model=LogisticRegression()
model.fit(X_train,y_train)
prediction=model.predict(X_test)
from sklearn.ensemble import RandomForestClassifier
rf_model=RandomForestClassifier()
rf_model.fit(X_train,y_train)
rf_prediction=rf_model.predict(X_test)

from sklearn.metrics import accuracy_score,classification_report
print("Accuracy:",accuracy_score(y_test,prediction)*100)
print(classification_report(y_test,prediction))

