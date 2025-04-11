class parallelogram:
    def __init__(self,height,base):
        self.height = height 
        self.base = base 

    def area(self):
        area = self.height*self.base
        print(area)


class triangles:
    def __init__(self,height,base):
        self.height = height
        self.base = base

    def area(self):
        area = self.base*self.height*1/2
        print(area)

triangleabc = triangles(4,3)
rhombusabcd = parallelogram(18,9)

x= (triangleabc,rhombusabcd)

for i in x:
    i.area()