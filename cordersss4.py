import geopandas as gpd
from geopandas.tools import geocode
import matplotlib.pyplot as plt
fp = r"TravelTimes_to_5975375_RailwayStation_Helsinki.geojson"
acc = gpd.read_file(fp)
#acc.head(2)
acc = acc.ix[acc['pt_r_tt'] >=0]
acc.plot(column="walk_d", scheme="Equal_Interval", k=9, cmap="bwr", linewidth=0);
plt.tight_layout()
