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
text = list()
for line in file:
    text.append(line.strip().split())

# print results
print("Day 3")
print()

file.close()
