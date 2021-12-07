import sys
import os
sys.path.insert(1, 'C:/Users/Isaiah Higgins/Documents/GitHub/2021AdventOfCode/IsaiahHiggins')
import Common as com
import numpy as np

sample = os.path.realpath('sample.txt')
real = os.path.realpath('Real.txt')

content = com.readAndCleanLine('Real.txt')
#content = com.readAndCleanLine('sample.txt')

class fish():
    def __init__(self, age, period, new):
        self.age = int(age)
        self.period = int(period)
        self.new = new
    # returns true if the fish birthed a fish
    def NewDay(self):
        if not self.new:
            self.age -= 1
            if self.age < 0:
                self.age = self.period
                self.birth = True
                return True
            else:
                return False
        else:
            self.new = False
            return False
            
# parse file
content = content[0].split(',')
school = []
new = 8
for age in content:
    school.append(fish(age, 6, False))

def printSchool(day):
    message = ""
    for mom in school:
        message = message + str(mom.age) + ","
    print("day " + str(day) + ": " + message[:-1])
# simulate time
days = 0
init= len(content)
for i in range(0, days):
    #printSchool(i)
    for mom in school:
        if mom.NewDay():
            school.append(fish(new, 6, True))
    print(i)

print(len(school))

# better solution
days = 256

# Define data structures
day_cycle = [0]*9

# Loads input data into data structures
def load_input():
    with open('sample.txt') as f:
        nums = f.readline().split(',')
        for n in nums:
            day_cycle[int(n)] += 1

# Utilizes the data within the data structures and produces a result
def manipulate_data():
    for day in range(days):
        for i in range(len(day_cycle) - 1):
            cur = day_cycle[i]
            day_cycle[i] = day_cycle[i+1]
            if i == 0:
                spawning = cur
        day_cycle[8] = spawning # spawn new fishes equal to the number of 0 fishes this cycle
        day_cycle[6] += spawning # "move" 0 fishes to cycle 6
    n = 0
    for count in day_cycle:
        n += count
    print(n)

load_input()
manipulate_data()
