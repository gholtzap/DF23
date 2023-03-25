import pandas as pd
import zipcodes
import geopandas as gpd
import matplotlib.pyplot as plt

# Read the CSV file
data = pd.read_csv('clients.csv')

# Convert the 'PostalCode' column to a string type and pad with zeros if necessary
data['PostalCode'] = data['PostalCode'].astype(str).str.zfill(5)

# Validate postal codes using the 'zipcodes' library and filter the data
data['ValidZip'] = data['PostalCode'].apply(lambda x: bool(zipcodes.matching(x)))
filtered_data = data[data['ValidZip'] & (data['AnnualIncome'].notnull()) & (data['AnnualIncome'] != 0)]

# Group by 'PostalCode' and compute the sum of 'AnnualIncome' for each group
grouped_data = filtered_data.groupby('PostalCode')['AnnualIncome'].sum().reset_index()

# Save the aggregated data to a new CSV file
grouped_data.to_csv('grouped_data.csv', index=False)


# import relevant data
nyc_map = gpd.read_file("MODZCTA_2010.shp")
stats=pd.read_csv("grouped_data.csv")

map_and_stats=nyc_map.merge(stats, on="MODZCTA")

fig, ax = plt.subplots(1, figsize=(8, 8))
plt.xticks(rotation=90)

map_and_stats.plot(column="Latest Rates", cmap="Reds", linewidth=0.4, ax=ax, edgecolor=".4")

bar_info = plt.cm.ScalarMappable(cmap="Reds", norm=plt.Normalize(vmin=0, vmax=120))
bar_info._A = []
cbar = fig.colorbar(bar_info)

ax.set_xlim(970000, 1010000)
ax.set_ylim(140000, 200000)
ax.axis("off")
