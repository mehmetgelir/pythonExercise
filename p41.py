import shapely
import matplotlib.pyplot as plt
from shapely.geometry.point import Point
from shapely.geometry import box
import random
import math


x = []
y = []
for i in range(0,1000):
	x.append(random.uniform(1,1000));
	y.append(random.uniform(1,1000));

for m in range(0,1000):
	a=random.uniform(0,1000)
	b=random.uniform(0,1000)
	w=random.uniform(0,100)
	h=random.uniform(0,100)
	f=box(a,b,a+w,b+h)
	x,y=f.exterior.coords.xy;

plt.figure()

o = input("Box Number1: ")
o = int(o)
p = input("Box Number2: ")
p = int(p)
for m in range(0,1):
	a=(o)
	b=(o)
	w=(p)
	h=(p)
	f=box(a,b,a+w,b+h)
	x,y=f.exterior.coords.xy;
	plt.fill(x,y, edgecolor='black', linewidth=0.5)

d = input("Point Number: ")
d = int(d)
for i in range(0,d):
	x.append(random.uniform(1,1000));
	y.append(random.uniform(1,1000));
	plt.plot(x[i],y[i],marker ='o')
	

	
plt.show()