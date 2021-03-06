import geopandas as gpd
import geoplot as gplt
import geoplot.crs as gcrs
import matplotlib.pyplot as plt

ny_census_tracts = gpd.read_file(gplt.datasets.get_path('ny_census'))
ny_census_tracts = ny_census_tracts.assign(
    percent_white=ny_census_tracts['WHITE'] / ny_census_tracts['POP2000']
)

gplt.choropleth(
    ny_census_tracts,
    hue='percent_white',
    cmap='Purples', linewidth=0.5,
    edgecolor='white',
    legend=True,
    projection=gcrs.AlbersEqualArea()
)
plt.title("Percentage White Residents, 2000")
plt.savefig("ny-state-demographics.png", bbox_inches='tight', pad_inches=0.1)
plt.show()
