from math import sqrt, prod
import sys
from scipy.spatial import KDTree
from scipy.cluster.hierarchy import DisjointSet
from heapq import *
from collections import defaultdict

def d(p1, p2):
    return sqrt(sum([(i-j)**2 for (i,j) in zip(p1,p2)]))


inputs = []
for line in open(sys.argv[1]).readlines():
    inputs.append([int(i) for i in line.split(",")])

tree = KDTree(inputs)

neighbor_heap = []
for i, pt in enumerate(inputs):
    q = tree.query(pt,2)
    distance = q[0][-1]
    neighbor = q[1][-1]
    neighbor_heap.append((distance, i, neighbor))

heapify(neighbor_heap)

num_neighbors_used = defaultdict(int)
pairs_used = set()

dju = DisjointSet(range(len(inputs)))
while True:
    d, p1, p2 = heappop(neighbor_heap)
    while (p1, p2) in pairs_used or (p2, p1) in pairs_used:
        num_neighbors_used[p1] += 1
        q = tree.query(inputs[p1], num_neighbors_used[p1] + 2)
        distance = q[0][-1]
        neighbor = q[1][-1]
        heappush(neighbor_heap, (distance, p1, neighbor))

        d, p1, p2 = heappop(neighbor_heap)

    pairs_used.add((p1, p2))

    num_neighbors_used[p1] += 1
    dju.merge(p1, p2)

    if dju.subset_size(0) == len(inputs):
        print(inputs[p1][0] * inputs[p2][0])
        break

    q = tree.query(inputs[p1], num_neighbors_used[p1] + 2)
    distance = q[0][-1]
    neighbor = q[1][-1]
    heappush(neighbor_heap, (distance, p1, neighbor))


#ss = [len(subset) for subset in dju.subsets()]
#print (prod(sorted(ss)[-3:]))
