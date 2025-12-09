from math import prod

file = open("6.input").readlines()

parsed = [[j for j in i.split(" ") if j] for i in file]

# part A
total = 0
ops = parsed[-1]
nums = parsed[:-1]
for i, op in enumerate(ops):
    if op == '+':
        total += sum([int(n[i]) for n in nums])
    if op == '*':
        total += prod([int(n[i]) for n in nums])
        
print(total)


# part B

rows = file[:-1]
num_groups = [[]]

for i in range(len(rows[0])):
    col = "".join([r[i] for r in rows])
    if col.strip() == "":
        num_groups.append([])
    else:
        num_groups[-1].append(int(col))

num_groups.pop()
total = 0
for nums, op in zip(num_groups, ops):
    if op == '+':
        total += sum(nums)
    else:
        total += prod(nums)

print(total)
