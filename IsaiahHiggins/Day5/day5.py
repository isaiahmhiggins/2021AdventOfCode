import sys
sys.path.insert(1, 'C:/Users/Isaiah Higgins/Documents/GitHub/2021AdventOfCode/IsaiahHiggins')
import Common as com
import numpy as np

class vent:
    def __init__(self, sx, sy, ex, ey):
        self.startx = int(sx)
        self.starty = int(sy)
        self.endx = int(ex)
        self.endy = int(ey)
        self.isLine = (sy == ey) or (sx == ex)

    def status(self):
        print("start: (" + str(self.startx) + "," + str(self.starty) + ")")
        print("end: (" + str(self.endx) + "," + str(self.endy) + ")")
        print("isLine: " + str(self.isLine))


content = com.readAndCleanLine('Real.txt')
#content = com.readAndCleanLine('sample.txt')
answer =0
vents = []
mapSize = 0

# parse file
for part in content:
    part = part.split('->')
    start = part[0].strip().split(',')
    end = part[1].strip().split(',')
    maxStart = max(start)
    maxEnd = max(end)
    totalMax = max(maxStart, maxEnd)
    if int(mapSize) < int(totalMax):
        mapSize = int(totalMax)
    vents.append(vent(start[0], start[1], end[0], end[1]))

# generate map
map = np.zeros((mapSize + 1, mapSize + 1), np.uint64)

def addCoord(sx, sy, ex, ey):
    map[sy, sx] += 1
    while(sx != ex or sy != ey):
        if(sx < ex):
            sx += 1
        elif(sx > ex):
            sx -= 1
        if(sy < ey):
            sy += 1
        elif(sy > ey):
            sy -= 1
        map[sy, sx] += 1

for vent in vents:
    if vent.isLine or True:
        addCoord(vent.startx, vent.starty, vent.endx, vent.endy)

answer = (map > 1).sum()
print(answer)
