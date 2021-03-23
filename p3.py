import shapely
import matplotlib.pyplot as plt
from shapely.geometry.point import Point
from shapely.geometry import LineString
from shapely.geometry import box
from shapely.geometry import Polygon
import random
import math

x=[];
y=[];
plt.figure()

for i in range(0,100):
	x.append(random.uniform(1,1000));
	y.append(random.uniform(1,1000));
	plt.plot(x[i],y[i], marker = 'o')

Line=LineString([(1, 2), (4, 5), (60, 17)]);
x,y = Line.coords.xy;
pnt = Point(5,9);
c1= pnt.buffer(20);
pnt2= Point(15,30);
print(pnt);


max=0
maxbox=box(0,0,1,1);
for k in range(0,1000,50):
	for j in range(0,1000,50):
		f=box(j,k,j+200,k+200);
		c=0;
		for i in range(0,100):
			pnt=Point(x[i],y[i])
			if f.contains(pnt) :
				c+=1;
		if c>=max:
			max=c;
			maxbox=f;

print(max);

for i in range(0,100):
	plt.plot(x[i],y[i], marker = 'o')
	
a,b=maxbox.exterior.coords.xy;
plt.plot(a,b);
plt.show()



for i in range (0,500):
	a=random.uniform(0,1000)
	b=random.uniform(0,1000)
	w=random.uniform(0,100)
    h=random.uniform(0,100)
	f=box(a,b,a+w,b+h)
	print(f.area);

if f.contains(pnt2):
	print("Covered");
else:
	print("Not Covered");


plt.figure()
x,y=c1.exterior.coords.xy;
plt.fill(x,y,edgecolor='black', linewidth=2.1)
x,y=f.exterior.coords.xy;
plt.fill(x,y,edgecolor='black', linewidth=2.1)
plt.plot(pnt2.x,pnt2.y,'r',marker = 'o');
#plt.plot(x,y)
plt.show()


"""poly = Polygon([(2.2, 4.2), (7.2, -25.1), (9.26, -2.456)]) 
x,y=poly.exterior.coords.xy;
plt.fill(x,y,edgecolor='black', linewidth=2.1)
"""

'''p1 = Point(10,10);
c1= p1.buffer(20);
x,y=c1.exterior.coords.xy;
#plt.fill(x,y,edgecolor='black', linewidth=2.1)

p2 = Point(25,25);
c2= p2.buffer(10);
x,y=c2.exterior.coords.xy;
#plt.fill(x,y,edgecolor='black', linewidth=2.1)


c3=c1.difference(c2);
x,y=c3.exterior.coords.xy;
plt.fill(x,y,edgecolor='black', linewidth=2.1)

plt.show()'''



