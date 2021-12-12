import sys
import os
sys.path.insert(1, 'C:/Users/Isaiah Higgins/Documents/GitHub/2021AdventOfCode/IsaiahHiggins')
import Common as com
import numpy as np

sample = os.path.realpath('sample.txt')
real = os.path.realpath('Real.txt')

#content = com.readAndCleanLine('Real.txt')
content = com.readAndCleanLine('sample.txt')

def bfs(start, end, second):
    # add start point to queue
    # store start point, set of visited small, and if we can visit twice
    que = [(start, set(), second)]
    # loop while anything is in que
    while que:
        # get elements from current node
        current, small, second = que.pop(0)
        # end case
        if current == end:
            yield 1
        # handle lower case
        elif current.islower():
            second &= current not in small
            small.add(current)
        # loop over all connected nodes and add unvisited ones
        for node in map.get(current, []):
            if node not in small or second:
                que.append((node, small.copy(), second))


map = {}

for line in content:
    s,e = line.split('-')
    if s != 'end' and e != 'start':
        map.setdefault(s, set()).add(e)
    if e != 'end' and s != 'start':
        map.setdefault(e, set()).add(s)

print('part1:', sum(bfs('start', 'end', False)))
print('part2:', sum(bfs('start', 'end', True)))