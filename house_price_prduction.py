import pandas as pd 
data=pd.read_csv("train.csv")
print(data.head())
print(data.info())
print(data.describe())
print(data.columns)
print(data.isnull().sum()) # This line was already present and correct.
print(data.shape)
print(data.dtypes)
print(data.select_dtypes(include=['object']).columns)
print(data.select_dtypes(include=['int64', 'float64']).columns)
numerical_cols = data.select_dtypes(include=['int64', 'float64']).columns   
print(data[numerical_cols].isnull().sum())
print(data.shape)



features = ["OverallQual", "GrLivArea", "GarageCars", 
 "TotalBsmtSF", "YearBuilt", "FullBath"]

X = data[features]
y = data["SalePrice"]

# missing fix
X = X.fillna(X.mean())

# split
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# scale
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# model
from sklearn.ensemble import RandomForestRegressor
model = RandomForestRegressor(n_estimators=200, max_depth=10)
model.fit(X_train, y_train)

# predict
y_pred = model.predict(X_test)

# evaluate
from sklearn.metrics import mean_absolute_error, r2_score

print("MAE:", mean_absolute_error(y_test, y_pred))
print("R2:", r2_score(y_test, y_pred))