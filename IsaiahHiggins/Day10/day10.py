import sys
import os
sys.path.insert(1, 'C:/Users/Isaiah Higgins/Documents/GitHub/2021AdventOfCode/IsaiahHiggins')
import Common as com
import numpy as np

sample = os.path.realpath('sample.txt')
real = os.path.realpath('Real.txt')

content = com.readAndCleanLine('Real.txt')
#content = com.readAndCleanLine('sample.txt')


invalid_line_score = 0
incomplete_line_scores = []
for line in content:
  opening_stack = []
  for char in line:
    # opening char
    if char in '[({<':
      opening_stack.append(char)
    # next closing char should match
    else:
      expected_match = opening_stack.pop()
      # line is currupted
      if char != {'(':')', '[':']', '{':'}', '<':'>'}[expected_match]:
        invalid_line_score += {')':3, ']':57, '}':1197, '>':25137}[char]
        break
  else:  # Line is incomplete
    incomplete_score = 0
    for char in opening_stack[::-1]:
      incomplete_score *= 5
      incomplete_score += {'[': 2, '(':1, '{':3, '<':4}[char]
    incomplete_line_scores.append(incomplete_score)

# answers
print(f'Part 1: {invalid_line_score}')
median_incomplete_score = sorted(incomplete_line_scores)[len(incomplete_line_scores)//2]
print(f'Part 2: {median_incomplete_score}')
