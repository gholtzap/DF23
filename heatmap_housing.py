import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

c1 = 'State'
c2 = 'Count'
# Read the CSV file
housing_data = pd.read_csv('data/housing_data.csv')

filtered_data = housing_data.query("Count != 0").dropna(subset=[c2])
filtered_data = filtered_data.query(f"{c2}>=300")

# Calculate the average annual income by state
state_avg_income = filtered_data.groupby(c1)[c2].mean().reset_index()

# Read the shapefile for US states
us_states = gpd.read_file('maps/usa-states-census-2014.shp')

# Merge the shapefile with the average annual income data
us_states_data = us_states.merge(state_avg_income, left_on='NAME', right_on=c1)

print("Unique values in the 'State' column:")
print(state_avg_income['State'].unique())

print("Unique values in the 'NAME' column:")
print(us_states['NAME'].unique())

# Plot / format the heatmap
fig, ax = plt.subplots(1, figsize=(20, 10))

# Read the boundary shapefile
us_boundary = gpd.read_file('maps/usa-states-census-2014.shp')

# Plot / format the heatmap
fig, ax = plt.subplots(1, figsize=(20, 10))

# custom color map
colors_housing = [
    
    (0/255, 200/255, 0/255) ,  # Lowest color
    (199/255, 192/255, 70/255),  # Middle color
    (200/255, 0/255, 0/255)# Highest color
]

cmap_housing = LinearSegmentedColormap.from_list("custom", colors_housing)

us_states_data.plot(column=c2, cmap=cmap_housing, linewidth=0.8, ax=ax, edgecolor='0.8', legend=True, legend_kwds={'label': "Frequency of Home Retention Issues", 'orientation': "horizontal", 'shrink': 0.5, 'pad': 0.02})
us_states_data.boundary.plot(ax=ax, linewidth=1, edgecolor='black')
ax.set_title('Frequency of Home Retention Issues by State', fontdict={'fontsize': 14}, pad=20)
ax.set_axis_off()
plt.tight_layout()
#plt.show()


#save as PNG
plt.savefig("heatmaps/housing_heatmap.png", dpi=300)