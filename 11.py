import sys
from collections import defaultdict
from copy import deepcopy

g = {}
g_inv = {}
nodes = set()

for line in open(sys.argv[1]).readlines():
    items = line.strip().split(" ")
    node = items[0][:-1]
    g[node] = items[1:]
    nodes.add(node)
    for i in items[1:]:
        nodes.add(i)

for n in nodes:
    g_inv[n] = []
    if n not in g:
        g[n] = []

for a, bs in g.items():
    for b in bs:
        g_inv[b].append(a)



ways = {"you": 0}

def topo_sort(g_inv):
    topo_sorted = []
    g_inv = {n: set(g_inv[n]) for n in g_inv}
    while len(topo_sorted) < len(nodes):
        for n in g_inv.keys():
            if len(g_inv[n]) == 0:
                topo_sorted.append(n)
                del(g_inv[n])
                break
        for e in g[n]:
            g_inv[e].remove(n)
    return topo_sorted


tsort = topo_sort(g_inv)

from pprint import pprint
#pprint(g_inv)
#print(tsort)

def paths_from(a, b):

    counts = defaultdict(int)
    counts[a] = 1
    for n in tsort:
        if n in counts:
            continue
        counts[n] = sum([counts[i] for i in g_inv[n]])
    return counts[b]

a = (paths_from("svr", "dac") * paths_from("dac", "fft") * paths_from("fft", "out"))
b = (paths_from("svr", "fft") * paths_from("fft", "dac") * paths_from("dac", "out"))

print(a,b)
