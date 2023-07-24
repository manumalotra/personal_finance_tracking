from fpdf import FPDF
import pandas as pd
import matplotlib.pyplot as plt
import analysis_functions as af
from datetime import date
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle, Image
from reportlab.lib.styles import getSampleStyleSheet

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

# Function to calculate the summary metrics for the current month
def calculate_summary_metrics(income_grouped, expenses_grouped):
    current_month = date.today().strftime("%Y-%m")
    total_income = income_grouped.get(current_month, 0)
    total_expenses = expenses_grouped.get(current_month, 0)
    net_income = total_income - total_expenses

    return total_income, total_expenses, net_income

# Function to generate the PDF report
def generate_pdf_report(income_df_path, expenses_df_path):
    # Read income and expenses data from CSV and group by year-month
    income_grouped = read_and_group_data(income_df_path)
    expenses_grouped = read_and_group_data(expenses_df_path)

    # Generate plots
    generate_plots(income_grouped, expenses_grouped, pd.read_csv(expenses_df_path))

    # Calculate the summary metrics for the current month
    total_income, total_expenses, net_income = calculate_summary_metrics(income_grouped, expenses_grouped)

    # Create PDF file using reportlab
    doc = SimpleDocTemplate("./example_report.pdf", pagesize=letter)

    # Report title
    styles = getSampleStyleSheet()
    report_title = Paragraph("Manu's Personal Finances Report", styles['Title'])
    report_date = Paragraph("Date: " + str(date.today()), styles['Normal'])
    report_author = Paragraph("Author: Manu Malotra", styles['Normal'])

    # Add all elements to the PDF
    elements = [report_title, report_date, report_author]

    # Add summary table to the PDF
    summary_data = [
        ['Metric', 'This Month'],
        ['Income Earned', total_income],
        ['Money Spent', total_expenses],
        ['Net Income', net_income]
    ]

    summary_table = Table(summary_data, colWidths=[2*inch, 1.5*inch])
    summary_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.gray),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ]))

    elements.append(summary_table)

    # Add images to the PDF
    image_paths = [
        './income_by_year_month.png',
        './expenses_by_year_month.png',
        './income_vs_expenses_by_year_month.png',
        './net_income_by_year_month.png',
        './categorized_expenses_by_year_month.png',
        './average_expenses_by_year_month.png'
    ]

    for image_path in image_paths:
        elements.append(Image(image_path, width=6*inch, height=3*inch))

    # Build the PDF
    doc.build(elements)

if __name__ == "__main__":
    # Update the file paths accordingly
    income_file_path = 'data_files/income.csv'
    expenses_file_path = 'data_files/expenses.csv'
    generate_pdf_report(income_file_path, expenses_file_path)
