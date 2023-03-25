import pandas as pd
import zipcodes

# Read the CSV file
data = pd.read_csv('clients.csv')

# Convert the 'PostalCode' column to a string type and pad with zeros if necessary

data['PostalCode'] = data['PostalCode'].astype(str).str.zfill(5)

#assert zipcodes.is_real()
filtered_data = data.query("AnnualIncome not in [0, 0.0] and PostalCode not in [0, 0.0]")

#filtered_data = data[(data['AnnualIncome'] != 0) & (data['PostalCode'] != 0)]

# Group by 'PostalCode' and compute the sum of 'AnnualIncome' for each group
grouped_data = data.groupby('PostalCode')['AnnualIncome'].sum().reset_index()

# Save the aggregated data to a new CSV file
grouped_data.to_csv('grouped_data.csv', index=False)
