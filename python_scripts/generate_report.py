from fpdf import FPDF
import pandas as pd
import matplotlib.pyplot as plt
import analysis_functions as af

# def group_data(dataframe):
#     '''Groups the income/expenses in the inputted DataFrame 
#     by Year-Month, and returns the grouped expenses.'''

#     # Convert 'Date' column to datetime
#     dataframe['Date'] = pd.to_datetime(dataframe['Date'])

#     # Extract year and month from 'Date' column
#     dataframe['Year-Month'] = dataframe['Date'].dt.to_period('M')

#     # Group income/expenses by yyyy-mm and calculate the sum
#     grouped_data = dataframe.groupby('Year-Month')['Amount'].sum()

#     return grouped_data

# def plot_data(grouped_data, data_type):
#     '''Plots income/expenses grouped by year-month on bar chart.'''

#     # Create a bar graph
#     grouped_data.plot(kind='bar')

#     # Set the labels and title based on data_type
#     if data_type == 'income':
#         plt.ylabel('Total Income')
#         plt.title('Income by Year-Month (YYYY-MM)')
#     elif data_type == 'expenses':
#         plt.ylabel('Total Expenses')
#         plt.title('Expenses by Year-Month (YYYY-MM)')

#     # Set the labels and title
#     plt.xlabel('Year-Month')

#     # Display the plot
#     # plt.show()

#     # Set the desired aspect ratio
#     aspect_ratio = 3/2   # Width:Height

#     # Set the figure size based on the desired aspect ratio
#     fig = plt.gcf()
#     fig.set_size_inches(10, 10 / aspect_ratio)  # Adjust the width and height accordingly

#     plt.savefig('./income_by_year_month.png', 
#                 transparent=False, 
#                 facecolor='white', 
#                 bbox_inches="tight")

# Read income and expenses data from CSV
income_df = pd.read_csv('data_files/income.csv')
expenses_df = pd.read_csv('data_files/expenses.csv')

# Group income and expenses data by year-month.
income_grouped = af.group_data(income_df)
expenses_grouped = af.group_data(expenses_df)

# Plot income by year-month.
af.plot_data(income_grouped, 'income')

# Plot expenses by year-month.
af.plot_data(expenses_grouped, 'expenses')

# Plot income and expenses by year-month.
af.plot_income_and_expenses(income_grouped, expenses_grouped)

# Plot net income by year-month.
af.plot_net_income(income_grouped, expenses_grouped)

# Plot categorized expenses by year-month.
af.plot_categorized_expenses(expenses_df)

##########################################################
#                    Create PDF file                     #
##########################################################

pdf = FPDF()
pdf.add_page()

pdf.set_font('Arial', 'B', 20)
pdf.cell(w=0, h=10, txt="Manu's Personal Finances Report", ln=1)

pdf.set_font('Arial', '', 16)
pdf.cell(w=30, h=10, txt="Date: ", ln=0)
pdf.cell(w=30, h=10, txt="2023-06-20", ln=1)
pdf.cell(w=30, h=10, txt="Author: ", ln=0)
pdf.cell(w=30, h=10, txt="Manu Malotra", ln=1)

# pdf.cell(w=30, h=10, txt="Income by Year-Month")
pdf.image('./income_by_year_month.png', 
          x = 25, y = None, w = 150, h = 0, type = 'PNG')

pdf.image('./expenses_by_year_month.png', 
          x = 25, y = None, w = 150, h = 0, type = 'PNG')

pdf.image('./income_vs_expenses_by_year_month.png', 
          x = 25, y = None, w = 150, h = 0, type = 'PNG')

pdf.image('./net_income_by_year_month.png', 
          x = 25, y = None, w = 150, h = 0, type = 'PNG')

pdf.image('./categorized_expenses_by_year_month.png', 
          x = 25, y = None, w = 150, h = 0, type = 'PNG')

pdf.output(f'./example.pdf', 'F')