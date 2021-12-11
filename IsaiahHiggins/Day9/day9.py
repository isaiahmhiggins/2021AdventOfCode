import sys
import os

from networkx.algorithms.centrality.load import newman_betweenness_centrality
sys.path.insert(1, 'C:/Users/Isaiah Higgins/Documents/GitHub/2021AdventOfCode/IsaiahHiggins')
import Common as com
import numpy as np

sample = os.path.realpath('sample.txt')
real = os.path.realpath('Real.txt')

#content = com.readAndCleanLine('Real.txt')
content = com.readAndCleanLine('sample.txt')

def compNeighbors(x, y, array):
    return (array[x, y] < array[x+1, y]) and (array[x, y] < array[x-1, y]) and (array[x, y] < array[x, y+1]) and (array[x, y] < array[x, y-1])

def basinSize(x, y, array):
    check = [(x, y)]
    array[x, y] = 9
    for line in check:
        if array[line[0]+1, line[1]] != 9:
            check += [(line[0]+1, line[1])]
            array[line[0]+1, line[1]] = 9
        if array[line[0]-1, line[1]] != 9:
            check += [(line[0]-1, line[1])]
            array[line[0]-1, line[1]] = 9
        if array[line[0], line[1]+1] != 9:
            check += [(line[0], line[1]+1)]
            array[line[0], line[1]+1] = 9
        if array[line[0], line[1]-1] != 9:
            check += [(line[0], line[1]-1)]
            array[line[0], line[1]-1] = 9
    return len(check)


for line in range(len(content)):
    content[line] = [char for char in content[line]]

content = np.array(content, np.uint64)
content = np.pad(content, [(1, 1), (1, 1)], mode = 'maximum')
locations = []
answer = 0
for x in range(1, np.size(content, 0) - 1):
    for y in range(1, np.size(content, 1) - 1):
        if(compNeighbors(x, y, content)):
            locations += [(x, y)]

sizes = []
for line in locations:
    sizes += [basinSize(line[0], line[1], content)]

sizes = sorted(sizes, reverse=True)
print(sizes)
print(sizes[0]* sizes[1] * sizes[2])