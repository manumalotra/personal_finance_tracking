from fpdf import FPDF
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

def plot_data(grouped_data, data_type):
    '''Plots income/expenses grouped by year-month on bar chart.'''

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

    # Display the plot
    # plt.show()

    plt.savefig('./income_by_year_month.png', 
                transparent=False,  
                facecolor='white', 
                bbox_inches="tight")

# Read income data from CSV
income_df = pd.read_csv('data_files/income.csv')

income_grouped = group_data(income_df)

# print(income_grouped)

# Plot income by year-month.
plot_data(income_grouped, 'income')

pdf = FPDF()
pdf.add_page()

pdf.set_font('Arial', 'B', 24)
pdf.cell(w=0, h=20, txt="Title", ln=1)
pdf.set_font('Arial', '', 16)
pdf.cell(w=30, h=50, txt="Date: ", ln=0)
pdf.cell(w=30, h=50, txt="2023-06-20", ln=1)
pdf.cell(w=30, h=50, txt="Author: ", ln=0)
pdf.cell(w=30, h=50, txt="Manu Malotra", ln=1)

pdf.image('./income_by_year_month.png', 
          x = 10, y = None, w = 100, h = 0, type = 'PNG')

pdf.output(f'./example.pdf', 'F')