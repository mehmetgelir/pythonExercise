import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
from geopandas.tools import geocode

fp = r"addresses.txt"
data = pd.read_csv(fp, sep=';')

geo = geocode(data['addr'], provider='nominatim')
#geo.head(2)
geo.plot()
join = geo.join(data)
join.head()
#join.plot()