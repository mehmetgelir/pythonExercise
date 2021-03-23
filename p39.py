import shapely
import matplotlib.pyplot as plt
from shapely.geometry.point import Point
from shapely.geometry import box
import random
import math

pnt = Point(5,9);
c1= pnt.buffer(20);
pnt2 = Point(18,20);

if c1.contains(pnt2):
	print("converd")
else:
	print("Not Converd")

plt.figure()
x,y=c1.exterior.coords.xy;
plt.fill(x,y, edgecolor='black', linewidth=0.5)
plt.plot(pnt2.x,pnt2.y,'r',marker = 'o');
plt.show()