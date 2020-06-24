import math
class Point:
    __x = 0
    __y = 0
    def __init__(self,x,y):
        self.__x = x
        self.__y = y
    def distance(self,point):
        distance = math.sqrt(math.pow((point.__x-self.__x),2)+math.pow((point.__y-self.__y),2))
        return distance
    def __add__(self,point):
        x = self.__x + point.__x
        y = self.__y + point.__y
        print('(',x,',',y,')')
   
p1 = Point(1,1)
p2 = Point(2,2)

print(p1.distance(p2))
p1+p2
        
