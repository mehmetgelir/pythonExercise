import pandas as pd
import geopandas as gpd
from shapely.geometry import Point, Polygon
import fiona
import matplotlib.pyplot as plt
from fiona.crs import from_epsg

newdata = gpd.GeoDataFrame()

newdata['geometry'] = None
coordinates =[(5,20),(25,11),(45,20)]
coordinates1 =[(12,5),(17,15),(25,11),(22,8)]
poly = Polygon(coordinates)
poly1 = Polygon(coordinates1)

newdata.loc[0,'geometry'] = poly
newdata.loc[1,'geometry'] = poly1
newdata.loc[0, 'location'] ='Karabük'
newdata.loc[1, 'location'] ='Bilecik'

newdata.crs = from_epsg(4326)
newdata.crs

newdata.plot()

