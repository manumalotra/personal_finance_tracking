import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

##########################################################
#                 Group income/expenses                  #
##########################################################

def group_data(dataframe):
    '''Groups the income/expenses in the inputted DataFrame 
    by Year-Month, and returns the grouped expenses.'''

    # Convert 'Date' column to datetime
    dataframe['Date'] = pd.to_datetime(dataframe['Date'])

    # Extract year and month from 'Date' column
    dataframe['Year-Month'] = dataframe['Date'].dt.to_period('M')

    # Group income/expenses by yyyy-mm and calculate the sum
    grouped_data = dataframe.groupby('Year-Month')['Amount'].sum()

    return grouped_data


##########################################################
#         Plot income or expenses on bar plot            #
##########################################################

def plot_data(grouped_data):
    '''Plots income/expenses grouped by year-month on bar chart.'''

    # Create a bar graph
    grouped_data.plot(kind='bar')

    # Set the labels and title
    plt.xlabel('Year-Month')
    plt.ylabel('Total Income')
    plt.title('Income by Year-Month')

    # Display the plot
    plt.show()


##########################################################
#      Plot income AND expenses on grouped bar plot      #
##########################################################

def plot_income_and_expenses(income_grouped, expenses_grouped):
    '''Plots income and expenses grouped by year-month on same bar chart.'''

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
    plt.show()


##########################################################
#            Plot net income on bar plot                 #
##########################################################

def plot_net_income(income_grouped, expenses_grouped):
    '''Plots net income by year-month on bar chart.'''

    # Calculate net income (income minus expenses)
    net_income_grouped = income_grouped - expenses_grouped

    # Create a bar graph for net income
    net_income_grouped.plot(kind='bar')

    # Set the labels and title
    plt.xlabel('Year-Month')
    plt.ylabel('Net Income')
    plt.title('Net Income by Year-Month')

    # Display the plot
    plt.show()


##########################################################
#           Plot ALL expenses on bar plot                #
##########################################################

def plot_all_expenses(expenses_df):
    '''Plots ALL recorded expenses on a bar chart, with each expense getting its own bar.
    I made this for fun to see if any pattern arises in my expenses. There is a clear 
    exponential decay pattern which follows the Pareto Principle.'''

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
#     Calculate total historic income and expenses       #
##########################################################

def total_income_and_expenses(income_df, expenses_df):
    '''Calculates total income and total expenses ever incurred, and calculates total net income.'''

    total_income = income_df['Amount'].sum()
    total_expenses = expenses_df['Amount'].sum()
    total_net_income = total_income - total_expenses

    return total_income, total_expenses, total_net_income


##########################################################
#  Print categorized expenses pivot table by year-month  #
##########################################################

def categorized_expenses_year_month(expenses_df):

    # Convert the 'Date' column to datetime type
    expenses_df['Date'] = pd.to_datetime(expenses_df['Date'])

    # Extract the year and month from the 'Date' column
    expenses_df['YearMonth'] = expenses_df['Date'].dt.to_period('M')

    # Group the data by 'YearMonth' and 'Category' and calculate the sum of 'Amount'
    # category_totals = expenses_df.groupby(['YearMonth', 'Category'])['Amount'].sum()

    # Create a pivot table to calculate the sum of 'Amount' for each 'YearMonth' and 'Category'
    category_totals = expenses_df.pivot_table(index='YearMonth', columns='Category', values='Amount', aggfunc='sum')

    # Print the category totals for each month
    print(category_totals)


##########################################################
#        Plot categorized expenses by year-month         #
##########################################################

def plot_categorized_expenses(expenses_df):

    ############################################
    #            Stacked bar plot              #
    ############################################

    # # Convert the 'Date' column to datetime
    # expenses_df['Date'] = pd.to_datetime(expenses_df['Date'])

    # # Extract the year and month from the 'Date' column
    # expenses_df['YearMonth'] = expenses_df['Date'].dt.to_period('M')

    # # Create a pivot table to get the total expenses in each category for each year-month
    # pivot_table = expenses_df.pivot_table(index='YearMonth', columns='Category', values='Amount', aggfunc='sum', fill_value=0)

    # # Plot the pivot table as a bar plot
    # pivot_table.plot(kind='bar', stacked=True, figsize=(10, 6))

    # # Set the labels and title
    # plt.xlabel('Year-Month')
    # plt.ylabel('Total Expenses')
    # plt.title('Categorized Expenses by Year-Month')

    # # Display the plot
    # plt.show()

    
    ############################################
    #           Stacked area plot              #
    ############################################

    # # Convert the Date column to datetime format
    # expenses_df['Date'] = pd.to_datetime(expenses_df['Date'])

    # # Extract year and month from the Date column
    # expenses_df['Year'] = expenses_df['Date'].dt.year
    # expenses_df['Month'] = expenses_df['Date'].dt.month

    # # Group the data by Year-Month and Category and sum the expenses
    # grouped_df = expenses_df.groupby(['Year', 'Month', 'Category'])['Amount'].sum().unstack()

    # # Create the stacked area plot
    # plt.figure(figsize=(12, 8))
    # grouped_df.plot.area(stacked=True)

    # # Customize the plot
    # plt.title('Categorized Expenses Over Time')
    # plt.xlabel('Year-Month')
    # plt.ylabel('Expenses')
    # plt.legend(title='Category', bbox_to_anchor=(1, 1))

    # # Rotate x-axis labels for better readability
    # plt.xticks(rotation=45)

    # # Display the plot
    # plt.show()


    ############################################
    #                Heatmap                   #
    ############################################

    # # Convert the Date column to datetime format
    # expenses_df['Date'] = pd.to_datetime(expenses_df['Date'])

    # # Extract year and month from the Date column
    # expenses_df['Year'] = expenses_df['Date'].dt.year
    # expenses_df['Month'] = expenses_df['Date'].dt.month

    # # Group the data by Year, Month, and Category and sum the expenses
    # grouped_df = expenses_df.groupby(['Year', 'Month', 'Category'])['Amount'].sum().reset_index()

    # # Pivot the data to have categories as columns and year-month as rows
    # pivot_df = grouped_df.pivot_table(values='Amount', index='Category', columns=['Year', 'Month'], fill_value=0)

    # # Add a row for Total Expenses
    # total_expenses = pivot_df.sum(axis=0)
    # pivot_df.loc['Total Expenses'] = total_expenses

    # # Create a heatmap
    # plt.figure(figsize=(12, 8))
    # sns.heatmap(pivot_df, cmap='YlGnBu')

    # # Customize the chart
    # plt.title('Categorized Expenses Heatmap')
    # plt.xlabel('Year-Month')
    # plt.ylabel('Category')

    # # Rotate the x-axis labels for better visibility
    # plt.xticks(rotation=90)

    # # Display the chart
    # plt.show()


    ############################################
    #          Categorized pie chart           #
    ############################################

    # # Convert the Date column to datetime format
    # expenses_df['Date'] = pd.to_datetime(expenses_df['Date'])

    # # Extract year and month from the Date column
    # expenses_df['Year'] = expenses_df['Date'].dt.year
    # expenses_df['Month'] = expenses_df['Date'].dt.month

    # # Group the data by Year, Month, and Category and sum the expenses
    # grouped_df = expenses_df.groupby(['Year', 'Month', 'Category'])['Amount'].sum().reset_index()

    # # Loop through each year-month and create a pie chart
    # for _, data in grouped_df.groupby(['Year', 'Month']):
    #     year, month = _
    #     categories = data['Category']
    #     expenses = data['Amount']

    #     # Create the pie chart
    #     plt.figure(figsize=(6, 6))
    #     plt.pie(expenses, labels=categories, autopct='%1.1f%%', startangle=90)

    #     # Customize the chart
    #     plt.title(f'Categorized Expenses - {year}-{month:02d}')

    #     # Display the chart
    #     plt.show()


    ############################################
    #         Categorized line chart           #
    ############################################

    # # Convert the Date column to datetime format
    # expenses_df['Date'] = pd.to_datetime(expenses_df['Date'])

    # # Extract year and month from the Date column
    # expenses_df['Year'] = expenses_df['Date'].dt.year
    # expenses_df['Month'] = expenses_df['Date'].dt.month

    # # Group the data by Category and Year-Month and sum the expenses
    # grouped_df = expenses_df.groupby(['Category', 'Year', 'Month'])['Amount'].sum().reset_index()

    # # Loop through each category and create a line chart
    # for category in expenses_df['Category'].unique():
    #     category_data = grouped_df[grouped_df['Category'] == category]
    #     year_month = category_data['Year'].astype(str) + '-' + category_data['Month'].astype(str).str.zfill(2)
    #     expenses = category_data['Amount']

    #     # Create the line chart
    #     plt.figure(figsize=(10, 6))
    #     plt.plot(year_month, expenses, marker='o')

    #     # Customize the chart
    #     plt.title(f'Expenses Over Time - Category: {category}')
    #     plt.xlabel('Year-Month')
    #     plt.ylabel('Expenses')

    #     # Rotate x-axis labels for better readability
    #     plt.xticks(rotation=45)

    #     # Display the chart
    #     plt.show()

    pass


##########################################################
#            Median spending by day of week              #
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


##########################################################
#         Plot net worth by year-month (yyyy-mm)         #
##########################################################