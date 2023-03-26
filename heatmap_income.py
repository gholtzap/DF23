import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
import numpy as np

c1 = 'StateName'
c2 = 'AnnualIncome'

# Read the CSV file
income_data = pd.read_csv('data/grouped_data.csv')

# Calculate the average annual income by state
state_avg_income = income_data.groupby(c1)[c2].mean().reset_index()

# Read the shapefile for US states
us_states = gpd.read_file('maps/usa-states-census-2014.shp')


# Merge the shapefile with the average annual income data
us_states_data = us_states.merge(state_avg_income, left_on='NAME', right_on=c1)

# Plot / format the heatmap
fig, ax = plt.subplots(1, figsize=(20, 10))

# custom color map

colors_income = [
    (255/255, 0/255, 0/255),  # Lowest color
    (199/255, 192/255, 70/255),  # Middle color
    (0/255, 255/255, 0/255)   # Highest color
]

cmap_income = LinearSegmentedColormap.from_list("custom", colors_income)

us_states_data.plot(column=c2, cmap=cmap_income, linewidth=0.8, ax=ax, edgecolor='0.8', legend=True, legend_kwds={'label': "Housing Issues Frequency", 'orientation': "horizontal", 'shrink': 0.5, 'pad': 0.02})
ax.set_title('Average Annual Income by State', fontdict={'fontsize': 14}, pad=20)
ax.set_axis_off()
plt.tight_layout()
plt.show()


# save as PNG
#plt.savefig("us_income_heatmap.png", dpi=300)