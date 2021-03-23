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
	w=random.uniform(0,100)
	h=random.uniform(0,100)
	f=box(a,b,a+w,b+h)
	print(f.area)
	x,y=f.exterior.coords.xy;
	plt.fill(x,y, edgecolor='black', linewidth=0.5)

plt.show()
