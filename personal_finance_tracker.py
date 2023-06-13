import pandas as pd

# Read expenses data from CSV
expenses_df = pd.read_csv('expenses.csv')

# Read income data from CSV
income_df = pd.read_csv('income.csv')

# Display the first few rows of each DataFrame
print("Expenses:")
print(expenses_df.head())
print("\nIncome:")
print(income_df.head())
