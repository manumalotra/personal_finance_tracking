import pandas as pd
import matplotlib.pyplot as plt
import analysis_functions as af

# Set the display options to show all rows and columns
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

##########################################################
#   Read CSV files containing income and expense data    #
##########################################################

# Read income data from CSV
income_df = pd.read_csv('data_files/income.csv')

# Read expenses data from CSV
expenses_df = pd.read_csv('data_files/expenses.csv')


##########################################################
#        Group income by year and month (yyyy-mm)        #
##########################################################

income_grouped = af.group_data(income_df)

# print(income_grouped)


##########################################################
#      Group expenses by year and month (yyyy-mm)        #
##########################################################

expenses_grouped = af.group_data(expenses_df)

# print(expenses_grouped)


##########################################################
#                   Basic accounting                     #
##########################################################

total_income, total_expenses, total_net_income = af.total_income_and_expenses(income_df, expenses_df)

# print(
# f"""
# Total income: {total_income}
# Total expenses: {total_expenses}
# Total net income: {total_net_income}
# """)


##########################################################
#          Plot income by year-month (yyyy-mm)           #
##########################################################

af.plot_data(income_grouped, 'income')


##########################################################
#        Plot expenses by year-month (yyyy-mm)           #
##########################################################

af.plot_data(expenses_grouped, 'expenses')


##########################################################
#    Plot income and expenses by year-month (yyyy-mm)    #
##########################################################

af.plot_income_and_expenses(income_grouped, expenses_grouped)


##########################################################
#         Plot net income by year-month (yyyy-mm)        #
##########################################################

af.plot_net_income(income_grouped, expenses_grouped)


##########################################################
#          Plot all expenses in descending order         #
##########################################################

# af.plot_all_expenses(expenses_df)


#################################################################
#   Categorized expenses by year-month (yyyy-mm) pivot table    #
#################################################################

# af.categorized_expenses_year_month(expenses_df)


##########################################################
#    Plot categorized expenses by year-month (yyyy-mm)   #
##########################################################

# af.plot_categorized_expenses(expenses_df)
