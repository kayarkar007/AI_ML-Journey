import pandas as pd
data = pd.read_csv("students.csv")
data["average"]=(data["maths"]+data["science"]+data["english"])
print(data)
topper= data.loc[data["average"].idxmax()]
print(topper)
sorted_data = data.sort_values(by="average", ascending=False)
print(sorted_data)


import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("students.csv")

# Average column
data["average"] = (data["maths"] + data["science"] + data["english"]) / 3

# Bar chart
plt.bar(data["name"], data["average"])
plt.xlabel("Students")
plt.ylabel("Average Marks")
plt.title("Student Performance")
plt.show()


import seaborn as pks

pks.barplot(x="name", y="average", data=data)
plt.show()



from sklearn.model_selection import train_test_split

X = data[["maths", "science", "english"]]  # input
y = data["average"]                      # output

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X_train, y_train)

predictions = model.predict(X_test)
print(predictions)

from sklearn.metrics import mean_squared_error

error = mean_squared_error(y_test, predictions)
print("Error:", error)


from sklearn.linear_model import LogisticRegression

# Create binary result for Logistic Regression
data["result"] = (data["average"] > 70).astype(int)
X_logic = data[["maths", "science", "english"]]
y_logic = data["result"]

model_logic = LogisticRegression()
model_logic.fit(X_logic, y_logic)
