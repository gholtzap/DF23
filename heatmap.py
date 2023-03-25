import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

c1 = 'StateName'
c2 = 'AnnualIncome'
# Read the CSV file
income_data = pd.read_csv('grouped_data.csv')

# Calculate the average annual income by state
state_avg_income = income_data.groupby(c1)[c2].mean().reset_index()

# Read the shapefile for US states
us_states = gpd.read_file('tl_2020_us_state.shp')

# Merge the shapefile with the average annual income data
us_states_data = us_states.merge(state_avg_income, left_on='NAME', right_on=c1)

# Plot the heatmap
fig, ax = plt.subplots(1, figsize=(15, 15))
us_states_data.plot(column=c2, cmap='coolwarm', linewidth=0.8, ax=ax, edgecolor='0.8', legend=True)
ax.set_title('Average Annual Income by State')
ax.set_axis_off()
plt.show()
