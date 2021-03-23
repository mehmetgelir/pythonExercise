import geopandas as gpd
import matplotlib.pyplot as plt

ULKE_KODU = gpd.read_file('C:/Users/Win10/Uygulama_01/Ulkeler.shp')
ULKE_KODU.plot(cmap = 'jet', column = 'ULKE_ADI', figsize = (10,10))

IL = gpd.read_file('C:/Users/Win10/Uygulama_01/Turkiye.shp')
IL.plot()   

fig, ax = plt.subplots(1)
ULKE_KODU.plot(ax=ax, cmap = 'rainbow', column = 'AD')
IL.plot(ax=ax, color = 'yellow')

#ULKE_KODU_in_IL = gpd.overlay(ULKE_KODU, IL, how = 'intersection')
#ULKE_KODU_in_IL.plot(figsize = (10,10), cmap = 'jet', column = 'ULKE_ADI')


