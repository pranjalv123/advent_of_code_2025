
input = "5.input"
sample= "5.sample"

ranges, qs = open(input).read().split("\n\n")

ranges = [[int(j) for j in i.split("-")] for i in ranges.split("\n")]
qs = [int(i) for i in qs.splitlines()]


ranges = sorted(ranges)

joined_ranges = [ranges[0]]
for (lo, hi) in ranges[1:]:
    cur_lo, cur_hi = joined_ranges[-1]
    if lo <= cur_hi:
        joined_ranges[-1] = cur_lo, max(hi, cur_hi)
    else:
        joined_ranges.append((lo, hi))

total = 0
for lo, hi in joined_ranges:
    total += hi - lo + 1

print(total)
