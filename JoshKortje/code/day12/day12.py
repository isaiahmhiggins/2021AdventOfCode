import numpy as np
import copy
import itertools
import networkx as nx
import string
import re
import math
import heapq
from scipy import ndimage
from functools import lru_cache
from collections import defaultdict
from collections import Counter
from collections import deque


# Start of script
file = open("input.txt", "r")

# Parse the file
text = list()
for line in file:
    text.append([int(x) for x in line.strip()])



# print results
print("Day 12")
print()

file.close()
