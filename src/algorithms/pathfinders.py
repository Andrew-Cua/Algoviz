from abc import ABC
from abc import abstractmethod

from typing import List

import math


class Vertex:
    index:int
    distance_from_source:int
    cost:int
    visited:bool
    x:int
    y:int
    precursor_vertex = None

    def __init__(self, index, cost, *args, **kwargs):
        self.index = index
        self.distance_from_source = math.inf
        self.cost = cost
        self.visited = False
        self.precursour_vertex = None

        self.x = kwargs.get('x')
        self.y = kwargs.get('y')

    def has_been_visited(self) -> bool:
        return self.visited

    def get_cost(self) -> int:
        return self.cost

    def get_dist_from_source(self) -> int:
        return distance_from_source

    def update_cost(self, cost):
        self.cost = cost

    def update_distance_from_source(self, dist):
        self.distance_from_source = dist

    def __str__(self):
        return "index:{}, distance:{}, \
visited:{}".format(self.index, self.distance_from_source, self.visited)

class Pathfinder(ABC):
    start_matrix:List[List[Vertex]]
    final_matrix:List[List[Vertex]]

    size:int

    def __init__(self):
        self.start_matrix = list()
        self.final_matrix = list()


    def set_size(self, size:int) -> None:
        self.size = size


    def initialize_start_matrix(self, start_matrix:List[List[int]]) -> None:
        self.size = len(start_matrix)

        count = 0
        for y in range(self.size):
            for x in range(self.size):
                if len(self.start_matrix) < y + 1:
                    self.start_matrix.append(list())
                self.start_matrix[y].append(Vertex(count, start_matrix[y][x],x=x,y=y))
                count = count + 1

    def init_default(self) -> None:
        self.size = 5

        for i in range(self.size * self.size):
            y = int(i / self.size)
            x = i % self.size

            if len(self.start_matrix) < y + 1:
                self.start_matrix.append(list())
            self.start_matrix[x].append(Vertex(i,1,x=x,y=y))

    def get_start_matrix(self) -> List[List[Vertex]]:
        return self.start_matrix

    @abstractmethod
    def solve(self) -> List[List[Vertex]]:
        pass

    @abstractmethod
    def get_path_to_vertex(self,x:int, y:int) -> str:
        pass



class DjikstraFinder(Pathfinder):

    def __init__(self):
        super(DjikstraFinder, self).__init__()

    def get_adj_vertex(self, vertex:Vertex) -> List[Vertex]:
        adj_verticies:List[Vertex] = list()

        x:int = vertex.x
        y:int = vertex.y
        if x > 0:
            adj_verticies.append(self.start_matrix[y][x-1])

        if x < self.size - 1:
            adj_verticies.append(self.start_matrix[y][x+1])

        if y > 0:
            adj_verticies.append(self.start_matrix[y-1][x])

        if y < self.size - 1:
            adj_verticies.append(self.start_matrix[y+1][x])

        return adj_verticies

    def solve(self) -> List[List[Vertex]]:
        solved: bool = False
        self.start_matrix[0][0].cost = 0
        self.start_matrix[0][0].distance_from_source = 0
        vertexes = [j for sub in self.start_matrix for j in sub]
        while not solved:

            ''' sort based on distance from source'''
            vertexes.sort(key=lambda e:e.distance_from_source)

            current_vertex:Vertex = None
            for vertex in vertexes:
                if vertex.has_been_visited():
                    pass
                else:
                    current_vertex = vertex
                    break

            ''' compute distance of  adj vertexes '''
            adjs = self.get_adj_vertex(current_vertex)

            for vertex in adjs:
                print(vertex)
                dist = current_vertex.distance_from_source + vertex.cost
                print("computing distance to {},{}, dist: {}".format(vertex.x,vertex.y,dist))
                if (dist <= vertex.distance_from_source):
                    vertex.distance_from_source = dist
                    vertex.precursor_vertex = current_vertex

            print(current_vertex)
            current_vertex.visited = True


            for vertex in vertexes:
                if vertex.has_been_visited() != True:
                    solved = False
                else:
                    solved = True

        for l in self.start_matrix:
            for vertex in l:
                print("Distance to {} is {}".format(vertex.index, vertex.distance_from_source))


    def get_path_to_vertex(self, x:int, y:int) -> str:
        path = [self.start_matrix[y][x]]

        start_found = False

        while start_found != True:
            current_vertex = path[0]
            if current_vertex.precursor_vertex == None:
                break
            else:
                path.insert(0,current_vertex.precursor_vertex)

        ret = ""
        xlist = []
        ylist = []
        for vertex in path:
            ret += "{}:{} ".format(vertex.x, vertex.y)
            xlist.append(vertex.x)
            ylist.append(vertex.y)

        return xlist, ylist


    class AStarFinder(Pathfinder):

        def __init__(self):
            super(AStarFinder, self).__init__()

        def solve(self) -> List[List[Vertex]]:
            #TODO extend vertex for A* since it needs to hold more data
            pass
