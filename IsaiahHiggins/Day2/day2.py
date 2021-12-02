import sys
sys.path.insert(1, 'C:/Users/Isaiah Higgins/Documents/GitHub/2021AdventOfCode/IsaiahHiggins')
import Common as com

content = com.readAndCleanLine('Real.txt')
#content = com.readAndCleanLine('sample.txt')
horiz = 0
depth = 0
aim = 0

for line in content:
    command = line.split(' ')
    instruction = command[0]
    x = int(command[1])
    if instruction == 'forward':
        horiz += x
        depth += aim * x
    elif instruction == 'up':
        aim -= x
    elif instruction == 'down':
        aim += x
print(depth*horiz)