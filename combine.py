import pandas as pd
import csv

# Read the CSV file
data = pd.read_csv('data/housing_data.csv')

# declare dicts
scores_housing = {
}

scores_income = {
}

# Storing column names as variables
column_count = 'Count'
column_state = 'State'
column_income_state = 'StateName'
column_income = 'AnnualIncome'

# Iterate through the rows of the data and add a key:value to the dict in the form of State:Value
for index, row in data.iterrows():
    scores_housing[row[column_state]] = row[column_count]

# Once we are done with housing_data, open next file  
data = pd.read_csv('data/grouped_data.csv')

# Same iteration as above
for index, row in data.iterrows():
    scores_income[row[column_income_state]] = row[column_income]

# ↓ Combining the two dicts created above ↓
combined_dict = scores_housing.copy()  # Start with a copy of dict1

for key, value in scores_income.items():
    if key in combined_dict:
        combined_dict[key] *= (1/value)  # If the key exists, multiply by the inverse of the income

print(combined_dict)

# Convert the dictionary to a pandas DataFrame

df = pd.DataFrame(list(combined_dict.items()), columns=['A', 'B'])
# Remove rows with a value of '0' in column B
df = df[df['B'] != 0]

# Save the DataFrame as a CSV file
df.to_csv('data/combined_data.csv', index=False)