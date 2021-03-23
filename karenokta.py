import shapely
import matplotlib.pyplot as plt
from shapely.geometry.point import Point
from shapely.geometry import box
import random



plt.figure()

f=box(0,0,200,200)

for i in range(0,200):
	a=random.uniform(0,1000)
	b=random.uniform(0,1000)
	w=random.uniform(0,200)
	h=random.uniform(0,200)
	f=box(a,b,a+w,b+h)
	x,y=f.exterior.coords.xy;
	plt.plot(x,y)
x = []
y = []
for i in range(0,200):
	x.append(random.uniform(1,1000));
	y.append(random.uniform(1,1000));
	plt.plot(x[i],y[i], marker = 'o')
    
    
plt.show()
