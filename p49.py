import shapely
import matplotlib.pyplot as plt
from shapely.geometry.point import Point
from shapely.geometry import box
from shapely.geometry import Polygon
import random
import math


f=Polygon([(5,20),(25,11),(45,20)])
x,y=f.exterior.coords.xy;
plt.fill(x,y,color='r', linewidth=2.1)
y=Polygon([(25,30),(17,15),(36,5)])
x,y=y.exterior.coords.xy;
plt.fill(x,y,color='r', linewidth=2.1)
y3=Polygon([(12,5),(17,15),(25,11)])
x,y=y3.exterior.coords.xy;
plt.fill(x,y,color='r', linewidth=2.1)




plt.show()



(30,30),(17,12),(35,5),(12,2),(17,12),(22,10)