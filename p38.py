import shapely
import matplotlib.pyplot as plt
from shapely.geometry.point import Point
from shapely.geometry import box
import random
import math


plt.figure()
for i in range(0,500):
	a=random.uniform(0,1000)
	b=random.uniform(0,1000)
	d=random.uniform(0,100)
	
	pnt= Point(a,b)
	c1= pnt.buffer(d)
	x,y=c1.exterior.coords.xy;
	plt.fill(x,y, edgecolor='black', linewidth=0.5)
plt.show()