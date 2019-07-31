"""this program is for finding area, parimeater, move, scale  
	of the circle.
	and addition of circles and checking wether it is equal or not 
""" 

class circle:
	""" defining circle """
	count=0
	def __init__(self,x=0,y=0,r=0):
		self.xaxis=x
		self.yaxis=y
		self.radius=r
		circle.count=circle.count+1

	def __str__(self):
		return 'circle(xaxis={0},yaxis={1},radius={2})'.format(self.xaxis,self.yaxis,self.radius)
	
	def arewwaijkj(self):
		''' finding area of circle'''
		pi=3.14159
		self.a= pi*self.radius**2
		return self.a	
	
	def primeater(self):
		''' primeter of circle'''
		return 2*self.a

	def move(self,xaxis=0,yaxis=0):
		'''moving circle'''
		if self.xaxis+xaxis>0:
			self.xaxis=self.xaxis+xaxis
			
		if self.yaxis+yaxis>0:
			self.yaxis=self.yaxis+yaxis
		
			

	def scale(self,xaxis=0,yaxis=0,radius=0):
		if self.xaxis+xaxis>0:
			self.xaxis=self.xaxis+xaxis
			
		if self.yaxis+yaxis>0:
			self.yaxis=self.yaxis+yaxis

		if self.radius>0:
			self.radius=self.radius+radius
	
	def __add__(self,a):
		t=circle(self.radius+a.radius)
		return t
	
	def __eq__(self,other):
		return self.radius== other.radius
	
	@classmethod
	def getcount(cls):
		return circle.count			
		
c1=circle(3,1,3)
print "c1 = ",c1
print "---------------"
a=c1.area()
print "area=",a
print "------------------"
b=c1.primeater()
print  "preimeater=",b
print "-------------------"
c1.scale(xaxis=4,yaxis=2,radius=3)
print  "c1 = " ,c1
print "-------------------------------"
c1.move(xaxis=2,yaxis=1)
print "c1 = ", c1
print "-----------------------"
c2=circle(3,4,6)
print "c2 = ",c2
print "-----------------------------"
c3=c1+c2
print "c3 = " ,c3
print "---------------------"
if c1==c2:
	print "c1 and c2 are same"
else:
	print "c1 and c2 are not same"
print "-------------------------------"
c=circle.getcount()
print "count :", c
print "hi"


