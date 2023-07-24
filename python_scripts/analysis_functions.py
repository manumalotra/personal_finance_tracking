import pandas as pd
import matplotlib.pyplot as plt

##########################################################
#                 Group income/expenses                  #
##########################################################

def group_data(dataframe):
    '''Groups the income/expenses in the inputted dataframe 
    by year-month, and returns the grouped expenses.'''

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

def plot_data(grouped_data, data_type):
    '''Plots income/expenses grouped by year-month on bar chart.'''

    # Create a new blank figure.
    plt.figure()

    # Create a bar graph
    grouped_data.plot(kind='bar')

    # Set the labels and title based on data_type
    if data_type == 'income':
        plt.ylabel('Total Income')
        plt.title('Income by Year-Month (YYYY-MM)')
    elif data_type == 'expenses':
        plt.ylabel('Total Expenses')
        plt.title('Expenses by Year-Month (YYYY-MM)')

    # Set the labels and title
    plt.xlabel('Year-Month')

    # Set the desired aspect ratio
    aspect_ratio = 2   # Width:Height

    # Set the figure size based on the desired aspect ratio
    fig = plt.gcf()
    fig.set_size_inches(10, 10 / aspect_ratio)  # Adjust the width and height accordingly

    if data_type == 'income':
        plt.savefig('./income_by_year_month.png', 
                    transparent=False, 
                    facecolor='white', 
                    bbox_inches="tight")
    elif data_type == 'expenses':
        plt.savefig('./expenses_by_year_month.png', 
                    transparent=False, 
                    facecolor='white', 
                    bbox_inches="tight")


##########################################################
#      Plot income AND expenses on grouped bar plot      #
##########################################################

def plot_income_and_expenses(income_grouped, expenses_grouped):
    '''Plots income and expenses grouped by year-month on same bar chart.'''

    # Merge expense and income data on 'YearMonth' column
    combined_df = pd.merge(expenses_grouped, income_grouped, on='Year-Month', how='outer').fillna(0)

    # Create a new blank figure.
    plt.figure()

    # Create a bar graph
    combined_df.plot(kind='bar')

    # Set the axis labels and title
    plt.xlabel('Year-Month')
    plt.ylabel('Amount')
    plt.title('Income vs. Expenses by Year-Month')

    # Add legend
    plt.legend(['Expenses', 'Income'])

    # Set the desired aspect ratio
    aspect_ratio = 2   # Width:Height

    # Set the figure size based on the desired aspect ratio
    fig = plt.gcf()
    fig.set_size_inches(10, 10 / aspect_ratio)  # Adjust the width and height accordingly

    plt.savefig('./income_vs_expenses_by_year_month.png', 
                    transparent=False, 
                    facecolor='white', 
                    bbox_inches="tight")


##########################################################
#            Plot net income on bar plot                 #
##########################################################

def plot_net_income(income_grouped, expenses_grouped):
    '''Plots net income by year-month on a bar chart.'''

    # Get a unique set of all year-month values from both income and expenses
    all_year_month = sorted(set(income_grouped.index) | set(expenses_grouped.index))

    # Calculate net income (income minus expenses) for all year-month values
    net_income_grouped = income_grouped.reindex(all_year_month, fill_value=0) - expenses_grouped.reindex(all_year_month, fill_value=0)

    # Set the x-values and y-values for the bar plot.
    x_values = net_income_grouped.index.astype(str)  # Convert the index to strings
    y_values = net_income_grouped.values

    # Create a new blank figure.
    plt.figure()

    # Create a bar plot.
    net_income_grouped.plot(kind='bar')

    # Set the labels and title
    plt.xlabel('Year-Month')
    plt.ylabel('Net Income')
    plt.title('Net Income by Year-Month')

    # Rotate the x-axis labels by 90 degrees
    plt.xticks(rotation=90)

    # Set the desired aspect ratio
    aspect_ratio = 2   # Width:Height

    # Set the figure size based on the desired aspect ratio
    fig = plt.gcf()
    fig.set_size_inches(10, 10 / aspect_ratio)  # Adjust the width and height accordingly

    plt.savefig('./net_income_by_year_month.png', 
                    transparent=False, 
                    facecolor='white', 
                    bbox_inches="tight")


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

    # Convert the 'Date' column to datetime
    expenses_df['Date'] = pd.to_datetime(expenses_df['Date'])

    # Extract the year and month from the 'Date' column
    expenses_df['YearMonth'] = expenses_df['Date'].dt.to_period('M')

    # Create a pivot table to get the total expenses in each category for each year-month
    pivot_table = expenses_df.pivot_table(index='YearMonth', columns='Category', values='Amount', aggfunc='sum', fill_value=0)

    # Plot the pivot table as a bar plot
    pivot_table.plot(kind='bar', stacked=True, figsize=(10, 6))

    # Set the labels and title
    plt.xlabel('Year-Month')
    plt.ylabel('Total Expenses')
    plt.title('Categorized Expenses by Year-Month')

    # Display the plot
    # plt.show()

    # Set the desired aspect ratio
    aspect_ratio = 2   # Width:Height

    # Set the figure size based on the desired aspect ratio
    fig = plt.gcf()
    fig.set_size_inches(10, 10 / aspect_ratio)  # Adjust the width and height accordingly

    plt.savefig('./categorized_expenses_by_year_month.png', 
                    transparent=False, 
                    facecolor='white', 
                    bbox_inches="tight")


def plot_expenses_rolling_average_bar_past_3_months(expenses_df):
    '''Plots the rolling average of expenses by year-month for the past 3 months as a bar chart.'''

    # Convert the Date column to datetime if it's not already in that format
    if not pd.api.types.is_datetime64_any_dtype(expenses_df['Date']):
        expenses_df['Date'] = pd.to_datetime(expenses_df['Date'])

    # Group the expenses by year-month
    grouped_data = expenses_df.groupby(pd.Grouper(key='Date', freq='M')).sum()

    # Calculate the rolling average for expenses using the past 3 months' data
    rolling_window = 3
    rolling_average = grouped_data['Amount'].rolling(window=rolling_window, min_periods=1).mean()

    # Create a new blank figure.
    plt.figure()

    # Plot the rolling average as a bar chart
    plt.bar(grouped_data.index, rolling_average, color='blue', width=20, label=f'{rolling_window}-Month Rolling Average')

    # Set the labels and title
    plt.xlabel('Year-Month')
    plt.ylabel('Expenses Rolling Average')
    plt.title(f'Rolling Average of Expenses by Year-Month (Past {rolling_window} Months)')

    # Add a legend
    plt.legend()

    # Set the desired aspect ratio
    aspect_ratio = 2   # Width:Height

    # Set the figure size based on the desired aspect ratio
    fig = plt.gcf()
    fig.set_size_inches(10, 10 / aspect_ratio)  # Adjust the width and height accordingly

    # Set x-axis tick positions and labels for all year-months
    plt.xticks(grouped_data.index, grouped_data.index.strftime('%Y-%m'), rotation=45, ha='right')

    plt.savefig('./average_expenses_by_year_month.png', 
                    transparent=False, 
                    facecolor='white', 
                    bbox_inches="tight")