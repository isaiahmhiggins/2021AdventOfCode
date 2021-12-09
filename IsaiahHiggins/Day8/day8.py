import sys
import os
sys.path.insert(1, 'C:/Users/Isaiah Higgins/Documents/GitHub/2021AdventOfCode/IsaiahHiggins')
import Common as com
import numpy as np
import itertools

sample = os.path.realpath('sample.txt')
real = os.path.realpath('Real.txt')

#content = com.readAndCleanLine('Real.txt')
content = com.readAndCleanLine('sample.txt')

# easy values
# 1, 4, 7, 8
easy = [2, 4, 3, 7]
answer = 0

# file content
for line in content:
    line = line.split('|')
    for char in line[1].split():
        if len(char) in easy:
            i = easy.index(len(char))
            answer += 1
      
print(answer)

map = {"acedgfb":8, "cdfbe":5, "gcdfa":2, "fbcad":3, "dab":7,
         "cefabd":9, "cdfgeb":6, "eafb":4, "cagedb":0, "ab":1}

map = {"".join(sorted(k)):v for k,v in map.items()}

answer = 0
for line in content:
    a,b = line.split(" | ")
    list = a.split(" ")
    word = b.split(" ")
    for perm in itertools.permutations("abcdefg"):
        # generate a mapping from the permutation
        pmap = {input:output for input,output in zip(perm,"abcdefg")}
        print(pmap)
        # generate new mapping
        listnew = ["".join(pmap[c] for c in char) for char in list]
        # generate new solution
        wordnew = ["".join(pmap[c] for c in char) for char in word]
        # check to see if the instance is correctly mapped
        if all("".join(sorted(an)) in map for an in listnew):
            # sort bnew so it will match the map
            wordnew = ["".join(sorted(x)) for x in wordnew]
            # decode map to get solution
            answer += int("".join(str(map[x]) for x in wordnew))
            break
print(answer)
