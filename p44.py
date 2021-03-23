import shapely
import matplotlib.pyplot as plt
from shapely.geometry.point import Point
from shapely.geometry import box
import random
import math

plt.figure()
for k in range(0,20):
	for m in range(0,20):
		f=box(m,k,m+200,k+200)
		
x,y=f.exterior.coords.xy;
plt.plot(x,y)
plt.show()