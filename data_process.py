import pandas as pd
import os 

# Load the data 
file_paths = ['./data/daily_sales_data_0.csv', './data/daily_sales_data_1.csv', './data/daily_sales_data_2.csv']
dataframes = []

for file in file_paths:
    df = pd.read_csv(file)

    # Filter for Pink Morsles only
    # sometimes the data might have capitalisation issues so we check for 'pink morsel'
    
    df = df[df['product'].str.lower() == 'pink morsel']

    # Create sales column 
    # we need to strip the '$' from the price and convert to float 

    df['price'] = df['price'].replace(r'[\$,]','',regex=True).astype(float)
    df['sales'] = df['price'] * df['quantity']

    # Keep only the required columns 
    df = df[['sales', 'date', 'region']]

    dataframes.append(df)

# Combine all three dataframes into one
combined_df = pd.concat(dataframes)

# Export to CSV
combined_df.to_csv('./data/combined_sales_data.csv', index=False)

print("Data processing complete! 'combined_sales_data.csv' has been created.")
