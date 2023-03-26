import pandas as pd
import numpy as np
import scipy.stats as st
from statsmodels.stats.power import TTestIndPower

c1 = 'StateName'
c2 = 'AnnualIncome'

# Read the CSV file
data = pd.read_csv('data/clients.csv')

# Filter out any 0 incomes | Reduces the dataset to about 330,000 to about 250,000
filtered_data = data.query("AnnualIncome != 0 & AnnualIncome <= 1000000 & AnnualIncome >=20000").dropna(subset=[c2])

filtered_data = filtered_data.query(f"{c2}>=300")

# Group by 'StateName' and compute the mean of 'AnnualIncome' for each group
grouped_data = filtered_data.groupby(c1)[c2].mean().reset_index()

print(grouped_data)

# Save the aggregated data to a new CSV file
grouped_data.to_csv('data/grouped_data.csv', index=False)

# print out all income values for a particular state 
state_data = filtered_data.query("StateName == 'Arizona'")
x = state_data[c2].tolist()


gd = data.groupby(c1)[c2].count().reset_index()
states_with_min_data_points = gd.query(f"{c2} >= 300")
#print(states_with_min_data_points)
