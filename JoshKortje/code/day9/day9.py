import numpy as np
import copy
import itertools
import networkx as nx
import string
import re
import math
import heapq
from functools import lru_cache
from collections import defaultdict
from collections import Counter


# Start of script
file = open("input.txt", "r")

# Parse the file
text = list()
for line in file:
    text.append(line.strip().split())



# print results
print("Day 9")
print()

file.close()