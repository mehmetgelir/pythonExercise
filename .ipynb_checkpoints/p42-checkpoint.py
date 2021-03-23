import shapely
import matplotlib.pyplot as plt
from shapely.geometry.point import Point
from shapely.geometry import box
import random
import math


plt.figure()
x = []
y = []
d = input("Point Number: ")
d = int(d)
for i in range(0,d):
	x.append(random.uniform(1,1000));
	y.append(random.uniform(1,1000));
	plt.plot(x[i],y[i],marker ='o')

o = input("Box Number1: ")
o = int(o)
p = input("Box Number2: ")
p = int(p)
max=0
maxbox=box(0,0,1,1);
for m in range(0,1):
	a=(o)
	b=(o)
	w=(p)
	h=(p)
	f=box(a,b,a+w,b+h)
	
x,y=f.exterior.coords.xy;
plt.plot(x,y)
plt.show()