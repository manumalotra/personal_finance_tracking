import pandas as pd
import matplotlib.pyplot as plt

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


def total_income_and_expenses(income_df, expenses_df):
    '''Calculates total income and total expenses ever incurred, and calculates total net income.'''

    total_income = income_df['Amount'].sum()
    total_expenses = expenses_df['Amount'].sum()
    net_income = total_income - total_expenses

    return total_income, total_expenses, net_income


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