import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

##########################################################
#   Read CSV files containing income and expense data    #
##########################################################

#Read income data from CSV
income_df = pd.read_csv('income.csv')

# Read expenses data from CSV
expenses_df = pd.read_csv('expenses.csv')


##########################################################
#                   Basic accounting                     #
##########################################################

total_income = income_df['Amount'].sum()
total_expenses = expenses_df['Amount'].sum()
net_income = total_income - total_expenses

# print("Total income:", total_income)
# print("Total expenses:", total_expenses)
# print("Net income:", net_income)


##########################################################
#      Group expenses by year and month (yyyy-mm)        #
##########################################################

# Convert 'Date' column to datetime
expenses_df['Date'] = pd.to_datetime(expenses_df['Date'])

# Extract year and month from 'Date' column
expenses_df['Year-Month'] = expenses_df['Date'].dt.to_period('M')

# Group expenses by yyyy-mm and calculate the sum
expenses_grouped = expenses_df.groupby('Year-Month')['Amount'].sum()

print("Expenses by Year-Month:")
print(expenses_grouped)


##########################################################
#        Plot spending by year-month (yyyy-mm)           #
##########################################################

# Create a bar graph
expenses_grouped.plot(kind='bar')

# Set the labels and title
plt.xlabel('Year-Month')
plt.ylabel('Total Spending')
plt.title('Spending by Year-Month')

# Display the plot
# plt.show()


##########################################################
#        Group income by year and month (yyyy-mm)        #
##########################################################

# Convert 'Date' column to datetime
income_df['Date'] = pd.to_datetime(income_df['Date'])

# Extract year and month from 'Date' column
income_df['Year-Month'] = income_df['Date'].dt.to_period('M')

# Group income by yyyy-mm and calculate the sum
income_grouped = income_df.groupby('Year-Month')['Amount'].sum()

print("\nIncome by Year-Month:")
print(income_grouped)