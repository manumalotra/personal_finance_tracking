import pandas as pd
import matplotlib.pyplot as plt
import analysis_functions as af

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

total_income, total_expenses, net_income = af.total_income_and_expenses(income_df, expenses_df)

# print("Total income:", total_income)
# print("Total expenses:", total_expenses)
# print("Net income:", net_income)


##########################################################
#      Group expenses by year and month (yyyy-mm)        #
##########################################################

expenses_grouped = af.group_data(expenses_df)

# print(expenses_grouped)


##########################################################
#        Plot spending by year-month (yyyy-mm)           #
##########################################################

# af.plot_data(expenses_grouped)


##########################################################
#        Group income by year and month (yyyy-mm)        #
##########################################################

income_grouped = af.group_data(income_df)

# print(income_grouped)


##########################################################
#          Plot income by year-month (yyyy-mm)           #
##########################################################

# af.plot_data(income_grouped)


##########################################################
#    Plot income and expenses by year-month (yyyy-mm)    #
##########################################################

# af.plot_income_and_expenses(income_grouped, expenses_grouped)


##########################################################
#         Plot net income by year-month (yyyy-mm)        #
##########################################################

# af.plot_net_income(income_grouped, expenses_grouped)


##########################################################
#          Plot all expenses in descending order         #
##########################################################

af.plot_all_expenses(expenses_df)


##########################################################
#         Plot net worth by year-month (yyyy-mm)         #
##########################################################




##########################################################
#              Median spend by day of week               #
##########################################################

# # Convert 'Date' column to datetime and extract day of the week
# expenses_df['DayOfWeek'] = expenses_df['Date'].dt.day_name()

# # Group expenses by day of the week and calculate the median spending
# daily_spending_median = expenses_df.groupby('DayOfWeek')['Amount'].median()

# # Create a bar graph for median daily spending
# daily_spending_median.plot(kind='bar')

# # Set the labels and title
# plt.xlabel('Day of the Week')
# plt.ylabel('Median Spending')
# plt.title('Median Daily Spending')

# # Display the plot
# # plt.show()