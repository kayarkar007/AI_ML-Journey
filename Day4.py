import pandas as pd

# Load data
data = pd.read_csv("students.csv")

# Step 1: Create average
data["average"] = (data["maths"] + data["science"] + data["english"]) / 3

# Step 2: Create pass/fail column
data["result"] = data["average"].apply(lambda x: 1 if x > 70 else 0)

print(data)

from sklearn.model_selection import train_test_split

X = data[["maths", "science", "english"]]  # features
y = data["result"]                        # target (pass/fail)


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)




from sklearn.linear_model import LogisticRegression

model = LogisticRegression()
model.fit(X_train, y_train)

predictions = model.predict(X_test)
print("Predictions:", predictions)

from sklearn.metrics import accuracy_score

accuracy = accuracy_score(y_test, predictions)*100
print("Accuracy:", accuracy)

new_student = [[85, 80, 78]]  # maths, science, english

result = model.predict(new_student)
print("Pass (1) / Fail (0):", result)