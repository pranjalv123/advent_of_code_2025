from sys import stdin

def parse(inp):
    for line in inp:
        yield line[0], int(line[1:])

def run(inp):
    pos = 50
    n_zero = 0

    prev_d = ""

    for d, q in parse(inp):
        pos0 = pos
        if d == 'R':
            pos += q
        if d == 'L':
            pos -= q
        n_zero+=abs(pos//100 - pos0//100)
        bonus = (pos0 % 100 == 0) and prev_d and (prev_d != d)
        if bonus:
            if d == 'R':
                n_zero += 1 
            if d == 'L':
                n_zero -= 1
        print(pos0, pos, d, abs(pos//100 - pos0//100), bonus)
        pos = pos % 100
        prev_d = d

    print(n_zero)


ex="""L50
R1
L1
R1
L1
L1""".splitlines()

run(stdin)
