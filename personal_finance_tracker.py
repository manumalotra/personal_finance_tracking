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


##########################################################
#          Plot income by year-month (yyyy-mm)           #
##########################################################

# Create a bar graph
income_grouped.plot(kind='bar')

# Set the labels and title
plt.xlabel('Year-Month')
plt.ylabel('Total Income')
plt.title('Income by Year-Month')

# Display the plot
# plt.show()


##########################################################
#    Plot income and expenses by year-month (yyyy-mm)    #
##########################################################

# Merge expense and income data on 'YearMonth' column
combined_df = pd.merge(expenses_grouped, income_grouped, on='Year-Month', how='outer').fillna(0)

# Create a bar graph
combined_df.plot(kind='bar')

# Set the labels and title
plt.xlabel('Year-Month')
plt.ylabel('Amount')
plt.title('Expenses vs. Income by Year-Month')

# Add legend
plt.legend(['Expenses', 'Income'])

# Display the plot
# plt.show()


##########################################################
#         Plot net income by year-month (yyyy-mm)        #
##########################################################

# Calculate net income (income minus expenses)
net_income = income_grouped - expenses_grouped

# Create a bar graph for net income
net_income.plot(kind='bar')

# Set the labels and title
plt.xlabel('Year-Month')
plt.ylabel('Net Income')
plt.title('Net Income by Year-Month')

# Display the plot
# plt.show()


##########################################################
#              Median spend by day of week               #
##########################################################

# Convert 'Date' column to datetime and extract day of the week
expenses_df['DayOfWeek'] = expenses_df['Date'].dt.day_name()

# Group expenses by day of the week and calculate the median spending
daily_spending_median = expenses_df.groupby('DayOfWeek')['Amount'].median()

# Create a bar graph for median daily spending
daily_spending_median.plot(kind='bar')

# Set the labels and title
plt.xlabel('Day of the Week')
plt.ylabel('Median Spending')
plt.title('Median Daily Spending')

# Display the plot
# plt.show()


##########################################################
#          Plot all expenses in descending order         #
##########################################################

# Sort expenses by amount in descending order
sorted_expenses = expenses_df.sort_values('Amount', ascending=False)

# Set the figure size to accommodate all bars
plt.figure(figsize=(12, 6))

# Create a bar graph for expenses
plt.bar(range(len(sorted_expenses)), sorted_expenses['Amount'], width=0.4)

# Set the labels and title
plt.xlabel('Expense Index')
plt.ylabel('Amount Spent')
plt.title('All Expenses (Descending Order)')

# Display the plot
plt.show()


##########################################################
#         Plot net worth by year-month (yyyy-mm)         #
##########################################################


