import sys
import os
sys.path.insert(1, 'C:/Users/Isaiah Higgins/Documents/GitHub/2021AdventOfCode/IsaiahHiggins')
import Common as com
import numpy as np
import itertools

sample = os.path.realpath('sample.txt')
real = os.path.realpath('Real.txt')

content = com.readAndCleanLine('Real.txt')
#content = com.readAndCleanLine('sample.txt')

def lightOn(x, y, array):
    index = list(itertools.product((0, -1, 1), repeat = 2))
    for xadd, yadd in index:
        if array[x + xadd, y + yadd] != 0 and array[x + xadd, y + yadd] != -1:
            array[x + xadd, y + yadd] += 1


def DayPartOne(array):
    for x in range(1, np.size(array, 0) - 1):
        for y in range(1, np.size(array, 1) - 1):
            array[x, y] += 1

def DayPartTwo(array):
    count = 0
    while np.amax(array) > 9:
        for x in range(1, np.size(array, 0) - 1):
            for y in range(1, np.size(array, 1) - 1):
                if array[x, y] > 9:
                    array[x, y] = 0
                    lightOn(x, y, array)
                    count += 1
    return count



for line in range(len(content)):
    content[line] = [char for char in content[line]]

content = np.array(content, np.int64)
content = np.pad(content, [(1, 1), (1, 1)],  mode='constant', constant_values='-1')


steps = 1000000
answer = 0
for step in range(steps):
    DayPartOne(content)
    answer += DayPartTwo(content)
    if np.count_nonzero(content == 0) == 100:
        answer = step
        break

print(answer+1)
    


    
