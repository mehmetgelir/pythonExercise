import shapely
import matplotlib.pyplot as plt
from shapely.geometry.point import Point
from shapely.geometry import LineString
import random
import math

Line=LineString([(1,2),(4,5),(60,17)]);
x,y = Line.coords.xy;


plt.figure()
plt.plot(x,y,marker ='o')
plt.show()