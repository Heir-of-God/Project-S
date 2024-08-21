t = int(input())

for _ in range(t):
    n = int(input())
    arr = [int(i) for i in input().split()]
    counter = {}
    for el in arr:
        if el not in counter:
            counter[el] = 0
        counter[el] += 1

    print(n - max(counter.values()))
