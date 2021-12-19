import numpy as np
import copy
import itertools
import networkx as nx
import string
import re
import math
import heapq
import binascii
import binarytree as bt
from scipy import spatial
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
    if '---' in line:
        text.append(list())
    elif line.strip():
        text[-1].append(tuple([int(x) for x in line.strip().split(',')]))




# print results
print("Day 20")
print()

file.close()
