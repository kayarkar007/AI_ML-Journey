import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor

# Load data
data = pd.read_csv("data/train.csv")

# Features
features = ["OverallQual", "GrLivArea", "GarageCars",
            "TotalBsmtSF", "YearBuilt", "FullBath"]

X = data[features]
y = data["SalePrice"]

# Handle missing
X = X.fillna(X.mean())

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Scaling
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)

# Model
model = RandomForestRegressor(n_estimators=200, max_depth=10)
model.fit(X_train, y_train)

# Save
pickle.dump(model, open("model/model.pkl", "wb"))
pickle.dump(scaler, open("model/scaler.pkl", "wb"))

print("Model + Scaler saved")