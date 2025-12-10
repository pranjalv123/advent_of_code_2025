import sys
from itertools import chain
import numpy as np
from scipy.optimize import milp, Bounds, LinearConstraint

def machines_a():
    machines = []
    for line in open(sys.argv[1]).readlines():
        line = line.strip()
        if not line:
            continue
        target_s, *switches_s = line.split(" ")
        joltage_s = switches_s.pop()
        target = int(target_s[1:-1].replace(".", "0").replace("#", "1")[::-1], 2)

        switches = []
        for s in switches_s:
            switches.append(sum([2**int(i) for i in s[1:-1].split(",")]))

        joltage = [int(i) for i in joltage_s[1:-1].split(",")]

        machines.append((target, switches, joltage))
    return machines
def solve_machine_a(target, switches, joltage):
    paths = {s: [s] for s in switches}
    new_paths = paths

    while True:
        new_new_paths = {}


        for a, path_a in chain(paths.items(), new_paths.items()):
            for b, path_b in new_paths.items():
                #print(bin(a), bin(b), bin(a^b))
                if a^b in paths and len(path_a) + len(path_b) >= len(paths[a^b]):
                    continue

                if a^b in new_paths and len(path_a) + len(path_b) >= len(new_paths[a^b]):
                    continue

                if a^b in new_new_paths and len(path_a) + len(path_b) >= len(new_new_paths[a^b]):
                    continue

                new_new_paths[a^b] = path_a + path_b


        paths.update(new_paths)
        new_paths = new_new_paths

        if target in paths:
            return paths[target]
        if target in new_paths:
            return new_paths[target]

        if not new_paths:
            raise RuntimeError()

def machines_b():
    machines = []
    for line in open(sys.argv[1]).readlines():
        line = line.strip()
        if not line:
            continue
        target_s, *switches_s = line.split(" ")
        joltage_s = switches_s.pop()
        target = target_s[1:-1]

        width = len(target)

        switches = []
        for s in switches_s:
            bits = [int(i) for i in s[1:-1].split(",")]
            switches.append(np.array([[0,1][i in bits] for i in range(width)]))

        joltage = np.array([int(i) for i in joltage_s[1:-1].split(",")])

        machines.append((target, np.array(switches).T, joltage))
    return machines


def solve_machine_b(target, switches, joltage):
    c = [1] * len(switches[0])
    bounds = Bounds(lb=[0] * len(switches[0]))
    integrality=[1] * len(switches[0])
    constraints = LinearConstraint(switches, joltage, joltage)
    

    result = milp(c, integrality=integrality, bounds=bounds, constraints=constraints)
    return sum(result.x)




total = 0
#for machine in machines_a():
#    total += len(solve_machine_a(*machine))

for machine in machines_b():
    total += int(solve_machine_b(*machine))
    #total += len(solve_machine_b(*machine))

print(total)
