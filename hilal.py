import shapely
import matplotlib.pyplot as plt
from shapely.geometry.point import Point
from shapely.geometry import box
from shapely.geometry import Polygon
import math


pnt= Point(24,34)
c1= pnt.buffer(45)
x,y=c1.exterior.coords.xy;


pnt1= Point(35,35)
c2= pnt1.buffer(35)
x,y=c2.exterior.coords.xy;


c3=c1.difference(c2);
x,y=c3.exterior.coords.xy;
plt.fill(x,y,color = 'r')

f=Polygon([(25,40),(45,31),(63,40)])
x,y=f.exterior.coords.xy;
plt.fill(x,y,color='r', linewidth=2.1)
y=Polygon([(45,50),(37,35),(56,25)])
x,y=y.exterior.coords.xy;
plt.fill(x,y,color='r', linewidth=2.1)
y3=Polygon([(32,25),(37,35),(45,31)])
x,y=y3.exterior.coords.xy;
plt.fill(x,y,color='r', linewidth=2.1)



plt.show()