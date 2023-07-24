from fpdf import FPDF
import pandas as pd
import matplotlib.pyplot as plt
import analysis_functions as af

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

# Plot rolling average of expenses by year-month (yyyy-mm)
af.plot_expenses_rolling_average_bar_past_3_months(expenses_df)

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

pdf.image('./income_by_year_month.png', 
          x = 10, y = None, w = 175, h = 0, type = 'PNG')

pdf.image('./expenses_by_year_month.png', 
          x = 10, y = None, w = 175, h = 0, type = 'PNG')

pdf.image('./income_vs_expenses_by_year_month.png', 
          x = 10, y = None, w = 175, h = 0, type = 'PNG')

pdf.image('./net_income_by_year_month.png', 
          x = 10, y = None, w = 175, h = 0, type = 'PNG')

pdf.image('./categorized_expenses_by_year_month.png', 
          x = 10, y = None, w = 175, h = 0, type = 'PNG')

pdf.output(f'./example.pdf', 'F')