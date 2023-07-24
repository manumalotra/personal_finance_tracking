from fpdf import FPDF
import pandas as pd
import matplotlib.pyplot as plt
import analysis_functions as af
from datetime import date

# Function to read data from CSV and group by year-month
def read_and_group_data(file_path):
    df = pd.read_csv(file_path)
    return af.group_data(df)

# Function to generate income and expenses plots
def generate_plots(income_grouped, expenses_grouped, expenses_df):
    af.plot_data(income_grouped, 'income')
    af.plot_data(expenses_grouped, 'expenses')
    af.plot_income_and_expenses(income_grouped, expenses_grouped)
    af.plot_net_income(income_grouped, expenses_grouped)
    af.plot_categorized_expenses(expenses_df)
    af.plot_expenses_rolling_average_bar_past_3_months(expenses_df)

# Function to generate the PDF report
def generate_pdf_report(income_df_path, expenses_df_path):
    # Read income and expenses data from CSV and group by year-month
    income_grouped = read_and_group_data(income_df_path)
    expenses_grouped = read_and_group_data(expenses_df_path)

    # Generate plots
    generate_plots(income_grouped, expenses_grouped, pd.read_csv(expenses_df_path))

    # Create PDF file
    pdf = FPDF()
    pdf.add_page()

    # Set font and report header
    pdf.set_font('Arial', 'B', 20)
    pdf.cell(w=0, h=10, txt="Manu's Personal Finances Report", ln=1)

    # Add report details
    pdf.set_font('Arial', '', 16)
    pdf.cell(w=30, h=10, txt="Date: ", ln=0)
    pdf.cell(w=30, h=10, txt=str(date.today()), ln=1)  # Display current date
    pdf.cell(w=30, h=10, txt="Author: ", ln=0)
    pdf.cell(w=30, h=10, txt="Manu Malotra", ln=1)

    # Add images to the PDF
    image_width = 175
    image_height = 0  # Automatic height to maintain aspect ratio
    image_paths = [
        './income_by_year_month.png',
        './expenses_by_year_month.png',
        './income_vs_expenses_by_year_month.png',
        './net_income_by_year_month.png',
        './categorized_expenses_by_year_month.png',
        './average_expenses_by_year_month.png'
    ]

    for image_path in image_paths:
        pdf.image(image_path, x=10, y=None, w=image_width, h=image_height, type='PNG')

    # Save the PDF report
    pdf.output('./example.pdf', 'F')

if __name__ == "__main__":
    # Update the file paths accordingly
    income_file_path = 'data_files/income.csv'
    expenses_file_path = 'data_files/expenses.csv'
    generate_pdf_report(income_file_path, expenses_file_path)
