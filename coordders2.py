import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
from geopandas.tools import geocode

fp = r"addresses.txt"
data = pd.read_csv(fp, sep=';')
#data.head()

c = input("Adres Giriniz ");
geo = geocode(c, provider='nominatim')
print(geo.head())
