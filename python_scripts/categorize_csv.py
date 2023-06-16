import pandas as pd

##########################################################
#   Read CSV files containing income and expense data    #
##########################################################

#Read income data from CSV
income_df = pd.read_csv('income.csv')

# Read expenses data from CSV
expenses_df = pd.read_csv('expenses.csv')


##########################################################
#      Retrieve all unique transaction descriptions      #
##########################################################

# Store the unique descriptions in an array.
unique_descriptions = expenses_df['Description'].unique()

# Alphabetically sort the unique descriptions.
unique_descriptions.sort()

dining = [
    'a&w', 'andaaz', 'around the corner', 'asian flame', 'baijiu',
    'boston pizza', 'bourbon street grill', 'central social hall',
    'chianti', 'chocorrant', 'chop sutton', 'chosun korean',
    'coco fresh', 'cosmic pizza', 'credo', 'denny\'s', 'dewey\'s',
    'dominos', 'donair', 'edo japan', 'el beso', 'gong cha',
    'hudsons whyte', 'jasper brewing', 'jarusalem shawarma', 
    'julio\'s barrio', 'la carraia', 'made by marcus', 'mcdonald\'s', 
    'menchie\'s', 'mikes famous', 'moxies bar', 'mr. sub', 'myhre', 
    'mogouyan hand pulled', 'namaste india', 'namsan korean', 
    'new everest', 'new york fries', 'opa of greece', 'popeyes', 
    'sandwich shop', 'rosso pizzeria', 'savoy`s express', 'shawarma house', 
    'sir winstons fish & chips', 'smitty\'s', 'coco\'s cafe', 'earls', 
    'hanjan', 'white rabbit ice', 'yelo?d ice cream', 'starbucks', 
    'steel wheels pizza', 'subway', 'teapsy', 'the alley brewery', 
    'the pint', 'the sherlock holmes', 'the sugar bowl', 'tim hortons', 
    'uber* eats', 'vegas donair', 'y-not indian', 'jerusalem shawarma',
    'seoul fried chicken', 'doordash', 'ubereats'
]

entertainment = [
    'albertaaviationmuseum', 'bird rides', 'bonnie doon bowling lanes', 
    'calgary tower', 'cineplex', 'edmonton heritage festiva', 
    'eventbrite', 'live it up lifestyle', 'lim*ride', 'landmark', 
    'laser city', 'marmot basin', 'muttart', 'park admissions', 
    'royal ab museum', 'spin scooter', 'activate edmonton', 'business students\'', 
    'edmonton expo ticket', 'gao badminton tao', 'lister hall', 
    'midway music hall', 'sustain su bike libra', 'calgary 6th avenue', 
    'taste of edmonton', 'tmcanada', 'wem marine life', 'www.f1.com', 
    'imaginus canada limited'
]

education = [
    'uofa bookstore', 'uofa business', 'uofa registrar', 'u of a onecard', 
    'ualberta bookstore', 'mcgraw-hill ryerson', 'cengage learning canada', 
    'stjohnambulance', 'livingworks'
]

sports = [
    'uofa ksr payments', 'decathlon', 'mountain warehouse', 'sport chek', 
    'everest outdoor stores', 'allsports & cycle', 'wild mountain jasper'
]

clothes = [
    'old navy', 'aldo', 'marshalls', 'h&m ca', 'zara', 'h & m ca', 'winners', 'russell jewellers'
]

housing = [
    'uofa residence'
]

grocery = [
    'wal-mart', 'fruiticana', 'safeway', 'save on foods', 
    'cdn tire', 'nofrills', 'brook\'s nf', 'dollarama', 
    'freson bros', 'h & w produce', 'wal*mart', 'real canadian sprst', 
    'instacart', 'shoppersdrugmart', 'ikea edmonton', 'h-mart u of a', 
    'shoppers drug mart', 'macs conv. stores', 'varsity drug'
]

subscription = [
    'fido', 'bell mobility', 'google*google storage', 'amazon.ca prime member', 
    'todoist', 'chefsplate', 'annual fee'
]

technology = [
    'source', 'apple.com/ca', 'best buy', 'staples'
]

transportation = [
    'rider express', 'busbud'
]

miscellaneous = [
    'amazon', 'amzn mktp', 'prime tax', 'long & mcquade', 
    'kanata trading post', 'drive-repmedia-axx', 'montanas', 
    'triton', 'students union'
]

# Loop through the unique descriptions
for description in unique_descriptions:
    # Convert the description to lowercase for case-insensitive matching
    lowercase_description = description.lower()

    for vendor in dining:
        if vendor in lowercase_description:
            expenses_df.loc[expenses_df['Description'] == description, 'Category'] = 'Dining'
    
    for vendor in entertainment:
        if vendor in lowercase_description:
            expenses_df.loc[expenses_df['Description'] == description, 'Category'] = 'Entertainment'
    
    for vendor in education:
        if vendor in lowercase_description:
            expenses_df.loc[expenses_df['Description'] == description, 'Category'] = 'Education'

    for vendor in sports:
            if vendor in lowercase_description:
                expenses_df.loc[expenses_df['Description'] == description, 'Category'] = 'Sports'
    
    for vendor in clothes:
        if vendor in lowercase_description:
            expenses_df.loc[expenses_df['Description'] == description, 'Category'] = 'Clothes'

    for vendor in housing:
        if vendor in lowercase_description:
            expenses_df.loc[expenses_df['Description'] == description, 'Category'] = 'Housing'
    
    for vendor in grocery:
        if vendor in lowercase_description:
            expenses_df.loc[expenses_df['Description'] == description, 'Category'] = 'Grocery'
    
    for vendor in subscription:
        if vendor in lowercase_description:
            expenses_df.loc[expenses_df['Description'] == description, 'Category'] = 'Subscription'
    
    for vendor in technology:
        if vendor in lowercase_description:
            expenses_df.loc[expenses_df['Description'] == description, 'Category'] = 'Technology'
    
    for vendor in transportation:
        if vendor in lowercase_description:
            expenses_df.loc[expenses_df['Description'] == description, 'Category'] = 'Transportation'
    
    for vendor in miscellaneous:
        if vendor in lowercase_description:
            expenses_df.loc[expenses_df['Description'] == description, 'Category'] = 'Amazon'

# Save the updated DataFrame to a new CSV file
expenses_df.to_csv('expenses2.csv', index=False)


# Set display options to show all columns and rows
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

# Read expenses data from CSV
expenses2_df = pd.read_csv('expenses2.csv')

# Create a boolean mask to check for empty values in the 'Category' column
mask = expenses2_df['Category'].isna()

# Filter the DataFrame using the mask to get the rows with missing category
missing_category_rows = expenses2_df[mask]

# Print the rows with missing category
print(missing_category_rows)