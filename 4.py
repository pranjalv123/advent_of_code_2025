import numpy as np
from scipy.signal import convolve2d
import sys

file = sys.argv[1]

symbols={'.': 0, '@':1}

def parse(inp):
    data = []
    for line in inp.splitlines():
        data.append([symbols[i] for i in line.strip()])
    return np.array(data)


initial_mat = parse(open(file).read())

kernel = np.array([[1,1,1], [1,1,1], [1,1,1]])


def solve(mat):

    conv = convolve2d(mat, kernel)

    neighbors = conv[1:-1,1:-1]

    roll_neighbors = neighbors * mat

    reachable = (roll_neighbors < 5) * (roll_neighbors > 0)

    return reachable.sum(), mat - reachable


total = 0
mat = initial_mat
while True:
    n, mat = solve(mat)
    if n == 0:
        print("!!")
        print(total)
        break
    print(n)
    total += n

