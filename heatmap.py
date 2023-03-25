import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

c1 = 'StateName'
c2 = 'AnnualIncome'
# Read the CSV file
income_data = pd.read_csv('data/grouped_data.csv')

# Calculate the average annual income by state
state_avg_income = income_data.groupby(c1)[c2].mean().reset_index()

# Read the shapefile for US states
us_states = gpd.read_file('maps/tl_2020_us_state.shp')

# Merge the shapefile with the average annual income data
us_states_data = us_states.merge(state_avg_income, left_on='NAME', right_on=c1)

# Plot the heatmap
fig, ax = plt.subplots(1, figsize=(15, 8))
us_states_data.plot(column=c2, cmap='coolwarm', linewidth=0.8, ax=ax, edgecolor='0.8', legend=True, legend_kwds={'label': "Average Annual Income", 'orientation': "horizontal", 'shrink': 0.5, 'pad': 0.02})
ax.set_title('Average Annual Income by State', fontdict={'fontsize': 14}, pad=20)
ax.set_axis_off()
plt.show()


# save as PNG
#plt.savefig("us_income_heatmap.png", dpi=300)