import shapely
import matplotlib.pyplot as plt
from shapely.geometry.point import Point
import random
import math


x = []
y = []
for i in range(0,1000):
	x.append(random.uniform(1,1000));
	y.append(random.uniform(1,1000));


plt.figure()

d = input("Point Number: ")
d = int(d)
for i in range(0,d):
	plt.plot(x[i],y[i],marker ='o')
plt.show()