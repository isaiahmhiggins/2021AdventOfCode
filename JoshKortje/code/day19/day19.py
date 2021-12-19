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


# To optimize I would need to store (for each beacon)
# the manhattan distances to the other beacons. Then get
# the intersections of the distances.


# Function to reorient to any direction
# I really hope this doesn't have a typo...
def get_orientations(beacon_list):
    # Hard coded because I really can't figure out a better way
    orientations = list()

    for beacon in beacon_list:
        this_orientation = list()
        # Facing positive x direction
        this_orientation.append((beacon[0], beacon[1], beacon[2]))
        this_orientation.append((beacon[0], beacon[2], -beacon[1]))
        this_orientation.append((beacon[0], -beacon[1], -beacon[2]))
        this_orientation.append((beacon[0], -beacon[2], beacon[1]))
        # Facing the negative x direction
        this_orientation.append((-beacon[0], -beacon[1], beacon[2]))
        this_orientation.append((-beacon[0], -beacon[2], -beacon[1]))
        this_orientation.append((-beacon[0], beacon[1], -beacon[2]))
        this_orientation.append((-beacon[0], beacon[2], beacon[1]))
        # Facing the positive y direction
        this_orientation.append((-beacon[1], beacon[0], beacon[2]))
        this_orientation.append((-beacon[2], beacon[0], -beacon[1]))
        this_orientation.append((beacon[1], beacon[0], -beacon[2]))
        this_orientation.append((beacon[2], beacon[0], beacon[1]))
        # Facing the negative y direction
        this_orientation.append((beacon[1], -beacon[0], beacon[2]))
        this_orientation.append((-beacon[2], -beacon[0], beacon[1]))
        this_orientation.append((-beacon[1], -beacon[0], -beacon[2]))
        this_orientation.append((beacon[2], -beacon[0], -beacon[1]))
        # Facing the positive z direction
        this_orientation.append((beacon[2], -beacon[1], beacon[0]))
        this_orientation.append((-beacon[1], -beacon[2], beacon[0]))
        this_orientation.append((-beacon[2], beacon[1], beacon[0]))
        this_orientation.append((beacon[1], beacon[2], beacon[0]))
        # Facing the negative z direction
        this_orientation.append((beacon[2], beacon[1], -beacon[0]))
        this_orientation.append((beacon[1], -beacon[2], -beacon[0]))
        this_orientation.append((-beacon[2], -beacon[1], -beacon[0]))
        this_orientation.append((-beacon[1], beacon[2], -beacon[0]))

        orientations.append(this_orientation)
    ordered = list(zip(*orientations))
    res = [x for x in ordered]
    return res


def get_shift(reference, loc):
    dx = reference[0] - loc[0]
    dy = reference[1] - loc[1]
    dz = reference[2] - loc[2]
    return dx, dy, dz


# Function to place the scanner in the reference space
def attempt_place(space, scanner, scanner_locations):
    # For each orientation possible
    for perspective in get_orientations(scanner):
        # For each point in the given perspective
        # Can skip 11 of them since if we haven't found a match after the
        # others it is impossible
        for point in perspective[11:]:
            # For each point we already know
            for ref in space:
                # Compare the points
                diff = get_shift(ref, point)
                shifted_points = [tuple(sum(x) for x in zip(spot, diff)) for spot in perspective]
                common = space.intersection(shifted_points)
                # If 12 or more points match, we have matched it with the reference frame
                if len(common) > 11:
                    space.update(shifted_points)
                    scanner_locations.append(diff)
                    return True
    return False


# Start of script
file = open("input.txt", "r")

# Parse the file
text = list()
for line in file:
    if '---' in line:
        text.append(list())
    elif line.strip():
        text[-1].append(tuple([int(x) for x in line.strip().split(',')]))


space = set(text.pop(0))
scanner_locations = [(0, 0, 0)]
space_dist = set()
for scan_a, scan_b in itertools.product(space, repeat=2):
    space_dist.add(spatial.distance.cityblock(scan_a, scan_b))

num_found = 1
while text:  # While we have unmatched scanners
    scanner = text.pop(0)
    # Try to place
    if attempt_place(space, scanner, scanner_locations):
        num_found += 1
        print(num_found)
    else:
        print('Miss')
        text.append(scanner)


# Part 2
# Calculate the max manhattan distance
distances = set()
for scan_a, scan_b in itertools.product(scanner_locations, repeat=2):
    distances.add(spatial.distance.cityblock(scan_a, scan_b))

# print results
print("Day 19")
print(len(space))
print(max(distances))

file.close()
