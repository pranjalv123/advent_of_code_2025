import sys
pts = []
for line in open(sys.argv[1]).readlines():
    x, y = [int(i) for i in line.split(",")]
    pts.append((x,y))


vertical_lines = []
horizontal_lines = []

for p1, p2 in zip(pts, pts[1:] + [pts[0]]):
    print(p1, p2)
    a, b = p1
    c, d = p2
    if a == c:
        vertical_lines.append((a, [b,d]))
    else:
        horizontal_lines.append((b, [a, c]))

vertical_lines.sort()
horizontal_lines.sort()

#print(horizontal_lines)
#print(vertical_lines)


def sign(a):
    if a < 0:
        return -1
    if a == 0:
        return 0
    if a > 0:
        return 1

def is_valid_rectangle(a, b, c, d):
    # a, b -> a, d
    bottom, top = sorted([b, d])
    left, right = sorted([a, c])

    for y, (p, q) in horizontal_lines:
        d = sign(p-q)
        p, q = sorted([p,q])
        if y < bottom or y > top:
            continue
        elif y > bottom and y  < top:
            if p < right and q > left:
#                print("a", y, p, q)
                return False
        elif y == bottom and d == 1:
#            print("b", y, p, q)
            return False
        elif y == top and d == -1:
#            print("c", y, p, q)
            return False

    for x, (p, q) in vertical_lines:
        d = sign(p-q)
        p, q = sorted([p,q])
        if x < left or x > right:
            continue
        elif x > left and x  < right:
            if p < top and q > bottom:
#                print("m", x, p, q)
                return False
        elif x == left and d == -1:
            if p < top and q < bottom:
#                print("n", x, p, q)
                return False
        elif x == right and d == 1:
            if p < top and q < bottom:
#                print("p", x, p, q)
                return False
    return True


sizes = []
for (a, b) in pts:
    for (c, d) in pts:
        if (a,b)==(c,d):
            continue
#        print(f"({a}, {b}) ({c}, {d}):")
        if is_valid_rectangle(a,b,c,d):
            sizes.append((1+abs(c-a)) * (1+abs(d-b)))
#            print(sizes[-1])


print(max(sizes))
