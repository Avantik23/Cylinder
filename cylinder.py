class Cylinder:

    def __init__(self,height=1,radius=1):
        self.h = height
        self.r = radius

    def volume(self):
        v = ((3.14) * (self.r **2)* self.h)
        print(v)

    def surface_area(self):
        s = (2*(3.14)*self.r) *(self.r+self.h)
        print(s)

       

c= Cylinder(2,3)    

c.volume()

c.surface_area()