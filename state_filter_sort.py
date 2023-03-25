import pandas as pd
import numpy as np

c1 = 'StateName'
c2 = 'AnnualIncome'

# Read the CSV file
data = pd.read_csv('data/clients.csv')

# Filter out any 0 incomes | Reduces the dataset to about 330,000 to about 250,000
filtered_data = data.query("AnnualIncome != 0 & AnnualIncome <= 1000000").dropna(subset=[c2])

# Group by 'StateName' and compute the mean of 'AnnualIncome' for each group
grouped_data = filtered_data.groupby(c1)[c2].mean().reset_index()

# Save the aggregated data to a new CSV file
grouped_data.to_csv('data/grouped_data.csv', index=False)
