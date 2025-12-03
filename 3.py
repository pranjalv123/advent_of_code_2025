def optimize_bank(numbers: list[int], size: int):
    if size == 1:
        return max(numbers)
    m = max(numbers[:-size+1])
    i = numbers.index(m)
    remainder = optimize_bank(numbers[i+1:], size-1)
    return remainder + m * (10**(size-1))


sample_input="""987654321111111
811111111111119
234234234234278
818181911112111"""

from sys import stdin

total = 0
for bank in stdin:
    bank = [int(i) for i in bank.strip()]
    opt = optimize_bank(bank, 12)
    print(bank)
    print(opt)
    print()
    total += opt

print(total)
