import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

from abc import ABC
from abc import abstractmethod

from algorithms.pathfinders import DjikstraFinder


class DataSRC():
    x_coords:list[int]
    y_coords:list[int]

    def __init__(self):
        self.x_coords = list()
        self.y_coords = list()


    def load_data(self) -> None:
        pass

    def get_data(self) -> tuple[list[int],list[int]]:
        return self.x_coords, self.y_coords


class FileSRC(DataSRC):
    location:str


    def __init__(self, location):
        super(FileSRC, self).__init__()
        self.location = location
        print(self.x_coords)

    def load_data(self) -> None:
        with open(self.location, 'r') as src:
            for line in src:
                coords = line.split(" ")
                for coord in coords:
                    self.x_coords.append(int(coord.split(':')[0]))
                    self.y_coords.append(int(coord.split(':')[1]))


class AlgorithimVisualizer:
    srcData: DataSRC

    def __init__(self, srcData:DataSRC):
        self.srcData = srcData

    def plotPath(self) -> None:
        self.srcData.load_data()
        x,y = self.srcData.get_data()

        plt.scatter(x,y)
        plt.show()




#src = FileSRC('test.txt')

#algo = AlgorithimVisualizer(src)


#algo.plotPath()






''' TODO refactor below into classes above'''

finder = DjikstraFinder()
finder.initialize_start_matrix([[1,1,1,1,1],
                                [12,12,12,12,1],
                                [1,1,1,1,1],
                                [1,12,12,12,12],
                                [1,1,1,1,1]])
finder.solve()
x,y = finder.get_path_to_vertex(4,4)


final_matrix = finder.start_matrix
fig, ax = plt.subplots()
for l in final_matrix:
    for vertex in l:
        ax.text(vertex.x,vertex.y, "{},{}".format(vertex.index, vertex.cost))

ax.plot(x,y)
plt.gca().invert_yaxis()
plt.show()
