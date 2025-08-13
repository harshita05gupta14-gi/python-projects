import pandas as pd
import matplotlib.pyplot as plt

# Load Excel data
df = pd.read_excel("sales_profit_category.xlsx", sheet_name="CombinedData")

# Subplots (1 row, 2 columns)
fig, axs = plt.subplots(1, 2, figsize=(12, 5))

# Line Chart - Monthly Sales & Profit
axs[0].plot(df['Month'], df['Sales (in ₹)'], marker='o', label='Sales', color='blue')
axs[0].plot(df['Month'], df['Profit (in ₹)'], marker='s', label='Profit', color='green')
axs[0].set_title('Monthly Sales and Profit')
axs[0].set_xlabel('Month')
axs[0].set_ylabel('Amount (in ₹)')
axs[0].legend()
axs[0].grid(True)

# Bar Chart - Category Distribution
category_counts = df['Category'].value_counts()
axs[1].bar(category_counts.index, category_counts.values, color='orange')
axs[1].set_title('Category Distribution')
axs[1].set_xlabel('Category')
axs[1].set_ylabel('Count')
axs[1].grid(axis='y')

# Adjust layout
plt.tight_layout()
plt.show()
