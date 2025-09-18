# revenue_prediction.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_percentage_error, r2_score
from xgboost import XGBRegressor

# Load datasets
customers = pd.read_csv("data/customers.csv")
employees = pd.read_csv("data/employees.csv")
offices = pd.read_csv("data/offices.csv")
orders = pd.read_csv("data/orders.csv")
order_details = pd.read_csv("data/order details.csv")
payments = pd.read_csv("data/payments.csv")
products = pd.read_csv("data/products.csv")
productlines = pd.read_csv("data/productlines.csv")

# Merge relevant datasets (simplified revenue-focused model)
df = orders.merge(order_details, on="orderNumber", how="left")
df = df.merge(customers, on="customerNumber", how="left")
df = df.merge(payments, on="customerNumber", how="left")

# Create target variable: revenue = quantity * price
df["revenue"] = df["quantityOrdered"] * df["priceEach"]

# Select features
X = df[["customerNumber", "productCode", "orderLineNumber", "creditLimit"]].fillna(0)
y = df["revenue"]

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model training
model = XGBRegressor(n_estimators=200, learning_rate=0.1, max_depth=6, random_state=42)
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluation
r2 = r2_score(y_test, y_pred)
mape = mean_absolute_percentage_error(y_test, y_pred)

print(f"R² Score: {r2:.2f}")
print(f"MAPE: {mape:.2%}")
print(f"Model Accuracy (approx): {100 * (1 - mape):.2f}%")
