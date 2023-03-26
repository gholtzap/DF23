import pandas as pd
import zipcodes

# Read the CSV file
data = pd.read_csv('data/clients_first2000.csv')

# Convert the 'PostalCode' column to a string type and pad with zeros if necessary
data['PostalCode'] = data['PostalCode'].astype(str).str.zfill(5)

# Remove any non-numeric characters from the 'PostalCode' column
data['PostalCode'] = data['PostalCode'].str.extract('(\d{5})', expand=False)

# Validate postal codes using the 'zipcodes' library and filter the data
data['ValidZip'] = data['PostalCode'].apply(lambda x: bool(zipcodes.matching(x)) if isinstance(x, str) else False)
filtered_data = data[data['ValidZip'] & (data['AnnualIncome'].notnull()) & (data['AnnualIncome'] != 0)]

# Group by 'PostalCode' and compute the sum of 'AnnualIncome' for each group
grouped_data = filtered_data.groupby('PostalCode')['AnnualIncome'].sum().reset_index()

# Save the aggregated data to a new CSV file
grouped_data.to_csv('data/grouped_data.csv', index=False)
