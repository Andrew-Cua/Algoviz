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

class Vector2d:
    x: float;
    y: float;

    def __init__(self, x:float, y:float) -> None:
        self.x = x;
        self.y = y;
        pass

    ''' returns the direction the vector is pointing '''
    def get_bearing(self) -> float:
        return 0.0

    ''' gets the magnitude of the vector '''
    def get_magnitude(self) -> float:
        return 0.0

    ''' returns a new vector that has magnitude of one'''
    def normalize(self) -> 'Vector2d': 
        x = self.x / self.get_magnitude()
        y = self.y / self.get_magnitude()
        return Vector2d(x, y)

    def dot(self, v:'Vector2d') -> float:
        dot = self.x * v.x + self.y * v.y

        return dot

class Path:
    start: Point
    end: Point

    ctrl_points: list[Point]

    def __init__(self, start:Point, end:Point) -> None:
        self.start = start
        self.end = end
        pass


    ''' gets the point on the path @ desired x coordinate'''
    def at_x(self, x:int) -> Point:
        '''TODO: implemment'''

        return Point(x,0)


    ''' get the distance between the agent and the path'''
    ''' TODO: look into using dot product to find distance from point on the line'''
    def dist_to_path(self, agent:Point) -> float:
        return 0.0



class Agent:
    position: Point
    vel_vec: Vector2d


    def __init__(self, x:int, y:int) -> None:
        self.position = Point(x,y)
        self.vel_vec = Vector2d(0,0)
        pass