from abc import ABC
from abc import abstractmethod
from typing import List
import math


'''TODOS 
    TODO: have agent follow straight line
    TODO: implemment cubic splines 
    TODO: have agent follow splines'''

class Point:
    x: int;
    y: int; 

    def __init__(self, x:int, y:int) -> None:
        self.x = x
        self.y = y
        pass

class Path:
    start: Point
    end: Point

    ctrl_points: list[Point]

    def __init__(self, start:Point, endPoint:Point) -> None:
        self.start = start
        self.end = end; 
        pass


    ''' gets the point on the path @ desired x coordinate'''
    def at_x(self, x:int) -> Point:
        '''TODO: implemment'''

        return Point(x,0)


    ''' get the distance between the agent and the path'''
    ''' TODO: look into using dot product to find distance from point on the line'''
    def dist_to_path(self, agent:Point) -> float:
        return 0.0
