import shapely
import matplotlib.pyplot as plt
from shapely.geometry.point import Point
from shapely.geometry import box
import random
import math


pnt= Point(10,10)
c1= pnt.buffer(20)
x,y=c1.exterior.coords.xy;
#plt.fill(x,y, edgecolor='black', linewidth=0.5)

pnt1= Point(30,30)
c2= pnt1.buffer(35)
x,y=c2.exterior.coords.xy;
#plt.fill(x,y, edgecolor='black', linewidth=0.5)

#c3=c1.intersection(c2);
#x,y=c3.exterior.coords.xy;
#plt.fill(x,y, edgecolor='black', linewidth=0.5)

#c3=c1.union(c2);
#x,y=c3.exterior.coords.xy;
#plt.fill(x,y, edgecolor='black', linewidth=0.5)

c3=c1.difference(c2);
x,y=c3.exterior.coords.xy;
plt.fill(x,y, edgecolor='black', linewidth=0.5)




plt.show()