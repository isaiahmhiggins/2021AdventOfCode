import numpy as np
import copy
import itertools
import networkx as nx
import string
import re
import math
import heapq
from collections import defaultdict


# Start of script
file = open("input.txt", "r")

# Split on every space
lines = list()
for line in file:
    lines.append(int(line.strip()))


# print results
print("Day 2")

file.close()
