import pandas as pd
# print(data.shape)
# print(data.head())
# print(data.info())
# print(data.describe())
# print(data.isnull().sum())


# Load data
data = pd.read_csv("students.csv")

# Feature engineering
data["average"] = (data["maths"] + data["science"] + data["english"]) / 3
data["result"] = data["average"].apply(lambda x: 1 if x > 70 else 0)

# Define features and target
X = data[["maths", "science", "english"]]
y = data["result"]

# Scaling
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train-test split
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42
)

# Model training
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(X_train, y_train)

# Prediction
predictions = model.predict(X_test)

# Evaluation
from sklearn.metrics import accuracy_score
print("Accuracy:", accuracy_score(y_test, predictions)*100)

import seaborn as sns
import matplotlib.pyplot as plt

sns.boxplot(data=data[["maths", "science", "english"]])
plt.show()