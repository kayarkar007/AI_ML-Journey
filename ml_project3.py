# Load data
import pandas as pd
data=pd.read_csv("Superstore.csv")

# Check the data 
print(data.head())
print(data.info())
print(data.describe())

#data featuring
data["Order Date"]= pd.to_datetime(data["Order Date"]);
data["Month"]=data["Order Date"].dt.to_period("M")
print(data["Order Date"].head(5))
print(data["Month"].head(5))

monthly_sales = data.groupby("Month")["Sales"].sum()

print(monthly_sales)

top_performing_month=data.groupby("Month")["Sales"].sum().sort_values(ascending=False).head(5)

print(top_performing_month)

top_selling_product=data.groupby("Product Name")["Sales"].sum().sort_values(ascending=False).head(5)

print(top_selling_product)

top_selling_category=data.groupby("Category")["Sales"].sum().sort_values(ascending=False).head(5)
print(top_selling_category)

less_selling_catrgory=data.groupby("Category")["Sales"].sum().sort_values(ascending=True).head(1)
print(less_selling_catrgory)

best_region=data.groupby("Region")["Sales"].sum().sort_values(ascending=False).head(1)
print(best_region)

region_sale=data.groupby("Region")["Sales"].sum()
print(region_sale)

discount_impact=data.groupby("Discount")["Sales"].sum().sort_values(ascending=False).head(5)    
print(discount_impact)

discount_profit=data.groupby("Discount")["Profit"].mean().sort_values(ascending=False).head(5)
print(discount_profit)

import matplotlib.pyplot as plt

monthly_sales.plot(kind="line")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()

region_sale.plot(kind="line")
plt.title("Region Sales")
plt.xlabel("Region")
plt.ylabel("Sales")
plt.show()

loss_products = data.groupby("Product Name")["Profit"].sum().sort_values().head(10)
print(loss_products)

plt.scatter(data["Discount"], data["Profit"])
plt.xlabel("Discount")
plt.ylabel("Profit")
plt.title("Discount vs Profit")
plt.show()
