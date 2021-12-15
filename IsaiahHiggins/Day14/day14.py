import sys
import os
sys.path.insert(1, 'C:/Users/Isaiah Higgins/Documents/GitHub/2021AdventOfCode/IsaiahHiggins')
import Common as com
import numpy as np

def most_frequent(List):
    return max(set(List), key = List.count)

def least_frequent(List):
    return min(set(List), key = List.count)

sample = os.path.realpath('sample.txt')
real = os.path.realpath('Real.txt')

content = com.readAndCleanLine('Real.txt')
#content = com.readAndCleanLine('sample.txt')

element = [char for char in content[0]]
map = {}
for line in content[2:]:
    current, next = line.split('->')
    map[current.strip()] = next.strip()

steps = 40
for j in range(steps):
    i = 0
    while i != len(element)-1:
        current = element[i] + element[i+1]
        element.insert(i+ 1, map.get(current))
        i += 2
    print(j)

mostCount = element.count(most_frequent(element))
leastCount = element.count(least_frequent(element))
print(mostCount - leastCount)

