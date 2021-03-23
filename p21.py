class Point:
	def __init__(self,x,y,z,color):
		self.x = x
		self.y = y
		self.z = z
		self.renk = color
p1 = Point(1,2,0,"purple")
p2 = Point(3,4,0,"red")
p3 = Point(5,6,0,"black")
print(p1.x)
print(p1.y)
print(p1.z)
print(p1.renk)

print(p2.x)
print(p2.y)
print(p2.z)
print(p2.renk)

print(p3.x)
print(p3.y)
print(p3.z)
print(p3.renk)