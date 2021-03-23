import geopandas as gpd
import matplotlib.pyplot as plt
import fiona

fp = "Europe_borders.shp"
data = gpd.read_file(fp)
data.plot()

#data.crs
#data['geometry'].head()

data_proj = data.copy()
data_proj = data_proj.to_crs(epsg=3035)
data_proj.plot()

#data_proj['geometry'].head()


#data.plot(facecolor='gray');
#plt.title("WGS84 projection");
#plt.tight_layout()
#data_proj.plot(facecolor='blue');
#plt.title("ETRS Lambert Azimuthal Equal Area projection");
#plt.tight_layout()
