import pandas as pd

# Read the CSV file
data = pd.read_csv('data/housing_data.csv')

# init array
scores_housing = {
}

scores_income = {
}

# Specify the column name you want to sum
column_count = 'Count'
column_state = 'State'
column_income_state = 'StateName'
column_income = 'AnnualIncome'

# Iterate through the rows of the DataFrame and add the value to the total variable
for index, row in data.iterrows():
    scores_housing[row[column_state]] = row[column_count]
    
data = pd.read_csv('data/grouped_data.csv')

for index, row in data.iterrows():
    scores_income[row[column_income_state]] = row[column_income]

combined_dict = scores_housing.copy()  # Start with a copy of dict1

for key, value in scores_income.items():
    if key in combined_dict:
        combined_dict[key] *= (1/value)  # If the key exists, add the value to the existing key

print(combined_dict)