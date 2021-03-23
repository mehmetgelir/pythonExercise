import shapely
import matplotlib.pyplot as plt
from shapely.geometry.point import Point
from shapely.geometry import box
import random
import math

pnt= Point(5,9);
c1= pnt.buffer(20);
plt.figure()
x,y=c1.exterior.coords.xy;
plt.plot(x,y)
plt.show()