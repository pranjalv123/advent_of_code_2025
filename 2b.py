from itertools import batched

def process_range(a:str, b:str, div: int):
    print()
    print(a, b, div)
    if len(a) % div != 0:
        a = '1' + '0' * (div * (1 + len(a)//div) - 1)
    if len(b) % div != 0:
        b = '9' * (div * (len(b)//div))

    if int(b) < int(a):
        return 0

    chunk_size = len(a)//div
    print(a, b, chunk_size)

    a_parts = [int(''.join(i)) for i in batched(a, chunk_size)]
    b_parts = [int(''.join(i)) for i in batched(b, chunk_size)]

    
    first_a = a_parts[0]
    first_b = b_parts[0]
    rest_a = a_parts[1:]
    rest_b = b_parts[1:]
    
    print(first_a, rest_a)
    print(first_b, rest_b)


    n = first_b - first_a
    print(n)

    a_inclusive = True
    for r in rest_a:
        if r < first_a:
            a_inclusive = True
            break
        if r > first_a:
            a_inclusive = False
            break

    b_inclusive = True
    for r in rest_b:
        if r > first_b:
            b_inclusive = True
            break
        if r < first_b:
            b_inclusive = False
            break

    print(a_inclusive, b_inclusive)


    if n == 0:
        if a_inclusive and b_inclusive:
            print(1)
            total= int( str(first_a) * div)
            for i in range(1, chunk_size):
                if len(set(batched(str(total), i))) == 1:
                    print("skipping", total, i)
                    return 0
            print("!", total)
            return total
        return 0


    starting = first_a
    if not a_inclusive:
        n -= 1
        starting += 1

    ending = first_b
    if b_inclusive:
        n += 1
        ending += 1

    print(f"{starting=}, {ending=}")

    total = 0
    if n > 0:
        for i in range(starting, ending):
            skipping=False
            for smaller in range(1, chunk_size):
                if len(set(batched(str(i)*div, smaller))) == 1:
                    print("skipping", str(i)*div)
                    skipping=True
                    break
            if skipping:
                continue
            print(str(i)*div)
            total += int(str(i) * div)


    print(n)
    print("!", total)

    return total

from sys import stdin

def process_all(inp):
    for line in inp:
        total = 0
        ranges = line.split(",")
        for r in ranges:
            a, b = r.strip().split("-")
            a, b = sorted([a, b], key=int)
            
            for div in range(2, len(b) + 1):

                total += process_range(a, b, div)

        print("!!!")
        print(total)


main_input=["61-71,12004923-12218173,907895-1086340,61083-74975,7676687127-7676868552,3328-4003,48-59,3826934-3859467,178-235,75491066-75643554,92-115,1487-1860,483139-586979,553489051-553589200,645895-722188,47720238-47818286,152157-192571,9797877401-9798014942,9326-11828,879837-904029,4347588-4499393,17-30,1-16,109218-145341,45794-60133,491-643,2155-2882,7576546102-7576769724,4104-5014,34-46,67594702-67751934,8541532888-8541668837,72-87,346340-480731,3358258808-3358456067,78265-98021,7969-9161,19293-27371,5143721-5316417,5641-7190,28793-36935,3232255123-3232366239,706-847,204915-242531,851-1135,790317-858666"]

sample_input=["11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"]

process_all(main_input)
