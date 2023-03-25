import pandas as pd
import zipcodes
import numpy as np

c1 = 'StateName'
c2 = 'AnnualIncome'

# Read the CSV file
data = pd.read_csv('data/clients_first2000.csv')

# Group by 'StateName' and compute the mean of 'AnnualIncome' for each group
grouped_data = data.groupby(c1)[c2].mean().reset_index()

# Save the aggregated data to a new CSV file
grouped_data.to_csv('data/grouped_data.csv', index=False)
