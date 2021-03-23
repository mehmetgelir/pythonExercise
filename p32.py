import shapely
import matplotlib.pyplot as plt
from shapely.geometry.point import Point

pnt=Point(6,9);
print(pnt);
plt.figure()
plt.plot(pnt.x,pnt.y,'b', marker = 'o')
plt.show()