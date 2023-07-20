import pandas as pd
import analysis_functions as af

# Set the display options to show all rows and columns
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)


# Read CSV files containing income and expense data:s

# Read income data from CSV and create income dataframe.
income_df = pd.read_csv('data_files/income.csv')

# Read expenses data from CSV and create expenses dataframe.
expenses_df = pd.read_csv('data_files/expenses.csv')

# Group income by year and month (yyyy-mm)
income_grouped = af.group_data(income_df)

# Group expenses by year and month (yyyy-mm)
expenses_grouped = af.group_data(expenses_df)

# Plot income by year-month (yyyy-mm)
af.plot_data(income_grouped, 'income')

# Plot expenses by year-month (yyyy-mm)
af.plot_data(expenses_grouped, 'expenses')

# Plot income and expenses by year-month (yyyy-mm)
af.plot_income_and_expenses(income_grouped, expenses_grouped)

# Plot net income by year-month (yyyy-mm)
af.plot_net_income(income_grouped, expenses_grouped)

# Plot categorized expenses by year-month (yyyy-mm)
af.plot_categorized_expenses(expenses_df)
