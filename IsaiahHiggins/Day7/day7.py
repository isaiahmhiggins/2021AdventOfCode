import sys
import os
sys.path.insert(1, 'C:/Users/Isaiah Higgins/Documents/GitHub/2021AdventOfCode/IsaiahHiggins')
import Common as com
import numpy as np

sample = os.path.realpath('sample.txt')
real = os.path.realpath('Real.txt')

content = com.readAndCleanLine('Real.txt')
#content = com.readAndCleanLine('sample.txt')

content = content[0].split(',')
content = np.array(content, np.uint64)

# create cost list
costs = np.zeros(int(max(content)) + 1, np.uint64)
costs[1] = 1
for i in range(2, len(costs)):
    costs[i] = costs[i-1] + i


def findHorizDist(guess, value):
    return(costs[abs(int(guess - value))])

distances = []
for guess in range(min(content), max(content)):
    dist = 0
    for value in content:
        dist += findHorizDist(guess, value)
    distances += [int(dist)]

print(min(distances))


