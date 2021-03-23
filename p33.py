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
for i in range(0,1000):
	plt.plot(x[i],y[i],marker ='o')
plt.show()