# Load Data
import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv("Superstore.csv")

# check and understand data 
print(data.shape)
print(data.head())
print(data.info())
print(data.describe())
data.columns=data.columns.str.strip()
print(data.isnull().sum())

# Data featuring
data["Order Date"]=pd.to_datetime(data["Order Date"])
data["Month"] = data["Order Date"].dt.to_period("M")

monthly_sales=data.groupby("Month")["Sales"].sum()

print(monthly_sales)
monthly_sales.plot(kind="line")
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.show()

data["Years"]=data["Order Date"].dt.to_period("Y")
yearly_sales=data.groupby("Years")["Sales"].sum()

yearly_sales.plot(kind="line")
plt.title("Yearly sales report")
plt.xlabel("Years")
plt.ylabel("Sales")
plt.show()

salesbycategory=data.groupby("Category")["Sales"].sum().sort_values()

salesbycategory.plot(kind="bar")
plt.title("sales by category")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.show()


profitbyproduct=data.groupby("Product Name")["Profit"].sum().sort_values().head()

profitbyproduct.plot(kind="barh")
plt.title("Profit by product")
plt.xlabel("Product Name")
plt.ylabel("Profit")
plt.show()

profitondiscount=data.groupby("Discount")["Profit"].mean()
profitondiscount.plot(kind="line")
plt.title("Profit on discount")
plt.xlabel("Discount")
plt.ylabel("Profit")
plt.show()

salesondiscount=data.groupby("Discount")["Sales"].sum()
salesondiscount.plot(kind="line")
plt.title("Sales on discount")
plt.xlabel("Discount")
plt.ylabel("Sales")
plt.show()
print("Highest Sales Month:", monthly_sales.idxmax())
print("Highest Sales Value:", monthly_sales.max())


# Define X and y
X = data[["Category","Sub-Category","Discount","Quantity"]]
y = data["Sales"]

# Encode categorical
X = pd.get_dummies(X, drop_first=True)

# Split
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)

# Scaling
from sklearn.preprocessing import StandardScaler
scaler=StandardScaler()

X_train=scaler.fit_transform(X_train)
X_test=scaler.transform(X_test)

# Model
from sklearn.linear_model import LinearRegression
model=LinearRegression()
model.fit(X_train,y_train)

# Prediction
prediction=model.predict(X_test)

# Evaluation
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

print("MAE:", mean_absolute_error(y_test, prediction))
print("MSE:", mean_squared_error(y_test, prediction))
print("R2 Score:", r2_score(y_test, prediction))