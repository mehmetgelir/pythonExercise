import shapely
import matplotlib.pyplot as plt
from shapely.geometry.point import Point
from shapely.geometry import box
from shapely.geometry import Polygon
import random
import math


poly=Polygon([(2.2,4.2),(7.2,-25.1),(9.26,-2.456),(2.-23,6.4),(7.2,-25.1),(5.26,-20.456)])		
x,y=poly.exterior.coords.xy;
plt.fill(x,y,edgecolor='black', linewidth=2.1)
plt.show()