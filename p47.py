import shapely
import matplotlib.pyplot as plt
from shapely.geometry.point import Point
from shapely.geometry import LineString
from shapely.geometry import box
from shapely.geometry import Polygon
import random
import math
plt.figure()


pnt1= Point(20,27)
c2= pnt1.buffer(20)
x,y=c2.exterior.coords.xy;
plt.fill(x,y, color='yellow', edgecolor='black', linewidth=5)


pnt= Point(20,27)
c1= pnt.buffer(7,5)
x,y=c1.exterior.coords.xy;
plt.fill(x,y, edgecolor='white', color='blue',  linewidth=5)



l= LineString([(5,40),(13,26)]);
x,y=l.coords.xy;
plt.plot(x,y,marker = 'o')

l2= LineString([(25,22),(21,7)]);
x,y=l2.coords.xy;
plt.plot(x,y,marker = 'o')

l1= LineString([(23,34),(37,37)]);
x,y=l1.coords.xy;
plt.plot(x,y,marker = 'o')

#y3=Polygon([(5,40),(13,26),(25,20),(22,7)])
#x,y=y3.exterior.coords.xy;
#plt.fill(x,y,color='black', linewidth=2.1)


'''c3 = c2.difference(c1);
x,y=c3.exterior.coords.xy;
plt.fill(x,y, edgecolor='black', linewidth=0.5)'''

plt.show()