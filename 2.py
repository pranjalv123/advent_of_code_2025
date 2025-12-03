def process_range(a:str, b:str):
    print()
    print(a, b)
    if len(a) % 2 != 0:
        a = '1' + '0' * len(a)
    if len(b) % 2 != 0:
        b = '9' * (len(b) - 1)

    print(a, b)
    
    first_half_a, second_half_a = int(a[:len(a)//2]), int(a[len(a)//2:])
    first_half_b, second_half_b = int(b[:len(b)//2]), int(b[len(b)//2:])

    print(first_half_a, second_half_a)
    print(first_half_b, second_half_b)

    n = first_half_b - first_half_a

    if n == 0:
        if second_half_a <= first_half_a and second_half_b >= first_half_b:
            print(1)
            total= int( str(first_half_a) * 2)
            print(total)
            return total
    starting = first_half_a
    if second_half_a > first_half_a:
        n -= 1
        starting += 1

    ending = first_half_b
    if second_half_b >= first_half_b:
        n += 1
        ending += 1

    print(f"{starting=}, {ending}")

    total = 0
    if n > 0:
        for i in range(starting, ending):
            print(str(i)*2)
            total += int(str(i) * 2)


    print(n)
    print(total)

    return total

from sys import stdin

def process_all(inp):
    for line in inp:
        total = 0
        ranges = line.split(",")
        for r in ranges:
            a, b = r.strip().split("-")
            a, b = sorted([a, b], key=int)

            total += process_range(a, b)
        print(total)


main_input=["61-71,12004923-12218173,907895-1086340,61083-74975,7676687127-7676868552,3328-4003,48-59,3826934-3859467,178-235,75491066-75643554,92-115,1487-1860,483139-586979,553489051-553589200,645895-722188,47720238-47818286,152157-192571,9797877401-9798014942,9326-11828,879837-904029,4347588-4499393,17-30,1-16,109218-145341,45794-60133,491-643,2155-2882,7576546102-7576769724,4104-5014,34-46,67594702-67751934,8541532888-8541668837,72-87,346340-480731,3358258808-3358456067,78265-98021,7969-9161,19293-27371,5143721-5316417,5641-7190,28793-36935,3232255123-3232366239,706-847,204915-242531,851-1135,790317-858666"]
process_all(main_input)
