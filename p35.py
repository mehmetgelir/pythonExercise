import shapely
import matplotlib.pyplot as plt
from shapely.geometry.point import Point
from shapely.geometry import LineString
import random
import math


x = []
y = []
for i in range(0,20):
	x.append(random.uniform(1,20));
	y.append(random.uniform(1,20));



plt.figure()

plt.plot(x,y,marker ='o')
plt.show()



 print("Polygon area at index {0} is: {1:.3f}".format(index, poly_area))