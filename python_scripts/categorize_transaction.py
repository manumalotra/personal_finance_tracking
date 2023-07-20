import pandas as pd
import vendors

##########################################################
#   Read CSV files containing income and expense data    #
##########################################################

# Read income data from CSV
# income_df = pd.read_csv('data_files/income.csv')

# Read expenses data from CSV
expenses_df = pd.read_csv('data_files/expenses.csv')


##########################################################
#      Retrieve all unique transaction descriptions      #
##########################################################

# Store the unique descriptions in an array.
unique_descriptions = expenses_df['Description'].unique()

# Alphabetically sort the unique descriptions.
unique_descriptions.sort()

# Loop through the unique descriptions
for description in unique_descriptions:
    # Convert the description to lowercase for case-insensitive matching
    lowercase_description = description.lower()

    for vendor in vendors.dining:
        if vendor in lowercase_description:
            expenses_df.loc[expenses_df['Description'] == description, 'Category'] = 'Dining'
    
    for vendor in vendors.entertainment:
        if vendor in lowercase_description:
            expenses_df.loc[expenses_df['Description'] == description, 'Category'] = 'Entertainment'
    
    for vendor in vendors.education:
        if vendor in lowercase_description:
            expenses_df.loc[expenses_df['Description'] == description, 'Category'] = 'Education'

    for vendor in vendors.sports:
            if vendor in lowercase_description:
                expenses_df.loc[expenses_df['Description'] == description, 'Category'] = 'Sports'
    
    for vendor in vendors.clothes:
        if vendor in lowercase_description:
            expenses_df.loc[expenses_df['Description'] == description, 'Category'] = 'Clothes'

    for vendor in vendors.housing:
        if vendor in lowercase_description:
            expenses_df.loc[expenses_df['Description'] == description, 'Category'] = 'Housing'
    
    for vendor in vendors.grocery:
        if vendor in lowercase_description:
            expenses_df.loc[expenses_df['Description'] == description, 'Category'] = 'Grocery'
    
    for vendor in vendors.subscription:
        if vendor in lowercase_description:
            expenses_df.loc[expenses_df['Description'] == description, 'Category'] = 'Subscription'
    
    for vendor in vendors.technology:
        if vendor in lowercase_description:
            expenses_df.loc[expenses_df['Description'] == description, 'Category'] = 'Technology'
    
    for vendor in vendors.transportation:
        if vendor in lowercase_description:
            expenses_df.loc[expenses_df['Description'] == description, 'Category'] = 'Transportation'
    
    for vendor in vendors.miscellaneous:
        if vendor in lowercase_description:
            expenses_df.loc[expenses_df['Description'] == description, 'Category'] = 'Amazon'

# Overwrite expenses.csv with updated DataFrame.
expenses_df.to_csv('data_files/expenses.csv', index=False)

# Set display options to show all columns and rows
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

# Read expenses data from CSV
expenses2_df = pd.read_csv('data_files/expenses.csv')

# Create a boolean mask to check for empty values in the 'Category' column
mask = expenses2_df['Category'].isna()

# Filter the DataFrame using the mask to get the rows with missing category
missing_category_rows = expenses2_df[mask]

# Print the rows with missing category
print(missing_category_rows)