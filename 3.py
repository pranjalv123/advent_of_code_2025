def optimize_bank(numbers:list[int], size: int):
    if size == 1:
        return max(numbers)
    i, m = max(enumerate(numbers[:-size+1]), key=lambda x: x[1])
    return m * (10**(size-1)) + optimize_bank(numbers[i+1:], size-1)

print(sum([optimize_bank([int(i) for i in bank.strip()], 12) for bank in open("3.input").readlines()]))
