import geopandas as gpd
import matplotlib.pyplot as plt

data = gpd.read_file("DAMSELFISH_distributions.shp")
#print(data.head());
selection = data[0:50]
data.plot();
plt.show()	