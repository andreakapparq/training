import math

class Point(object):
    def __init__(self,x=0,y=0):
        self.__x = x
        self.__y = y

    def distance_to(self,b):
        return abs(self.__x - b.__x) + abs(self.__y - b.__y)

def manhattan_distance(a: Point,b: Point) -> int:
    return a.distance_to(b)
