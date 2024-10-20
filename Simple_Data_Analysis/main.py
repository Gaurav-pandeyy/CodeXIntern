import pandas as pd

# Importing the dataset
df = pd.read_csv("cafe_orders_month.csv")

# 1. Calculating the average total price
average_price = df['Total Price'].mean()
print(f"{'-'*40}\nStatistics Overview\n{'-'*40}")
print(f"1. Average of Total Price: ${average_price:.2f}")

# 2. Finding the maximum amount spent by a customer in a day
max_price = df['Total Price'].max()
print(f"2. Maximum amount spent by a customer in a day: ${max_price:.2f}")

# 3. Finding the minimum amount spent by a customer
min_price = df['Total Price'].min()
print(f"3. Minimum amount spent by a customer: ${min_price:.2f}")

# 4. Finding the highest total amount spent by a customer in the month
total_spending = df.groupby('Customer Name')['Total Price'].sum().reset_index()
max_spender = total_spending.loc[total_spending['Total Price'].idxmax()]

print(f"\n{'-'*40}\nCustomer Spending Overview\n{'-'*40}")
print(f"4. Customer with the highest total spending in a month:")
print(f"   Customer Name: {max_spender['Customer Name']}")
print(f"   Total Amount Spent: ${max_spender['Total Price']:.2f}")

# 5. Finding the most used payment method
payment_counts = df['Payment Method'].value_counts()
most_common_payment = payment_counts.idxmax()

print(f"\n{'-'*40}\nPayment Method Insights\n{'-'*40}")
print(f"5. Most used payment method: {most_common_payment}")
print(f"   Used {payment_counts[most_common_payment]} times")

# Final visual separation
print(f"{'-'*40}")
