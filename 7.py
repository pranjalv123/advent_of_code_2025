import sys
import re
from collections import defaultdict

lines = open("7.input").readlines()


def findall(l, x):
    return [i[0] for i in enumerate(l) if i[1] == x]

laser_positions = defaultdict(int)
total = 0
for line in lines:
    seen = set()
    s_positions = set(findall(line, 'S'))
    for s in s_positions:
        laser_positions[s] = 1
    emitter_positions = findall(line, '^')
    for emitter in emitter_positions:
        if emitter in laser_positions:
            laser_positions[emitter+1] += laser_positions.get(emitter, 0)
            laser_positions[emitter-1] += laser_positions.get(emitter, 0)
            laser_positions[emitter] = 0

print(sum(laser_positions.values()))
