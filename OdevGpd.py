import geopandas as gpd
import matplotlib.pyplot as plt


fp = "DAMSELFISH_distributions.shp"
data = gpd.read_file(fp)
#data.plot()
      
selection = data
c = input("Sayiyi Giriniz ");
c = int(c)
newdata=gpd.GeoDataFrame()

newdata['geometry'] = None

k=0;
for index, row in selection.iterrows():
    poly_area = row['geometry'].area
       
    if poly_area > c:
        newdata.loc[k,'geometry'] = row['geometry']
        k=k+1;
newdata.plot()

      