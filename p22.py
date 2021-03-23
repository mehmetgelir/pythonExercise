class Point:
	def __init__(self,x,y,z,color):
		self.x = x
		self.y = y
		self.z = z
		self.color = color
	def Yazdir(self):
		print(self.x)
		print(self.y)
		print(self.z)
		print(self.color)

p1 = Point(1,2,0,"purple")
p2 = Point(3,4,0,"red")
p3 = Point(5,6,0,"black")
p1.Yazdir()
p2.Yazdir()
p3.Yazdir()