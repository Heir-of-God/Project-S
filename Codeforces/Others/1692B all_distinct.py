t = int(input())

for _ in range(t):
    n = int(input())
    a = [int(i) for i in input().split()]
    uniq = 0
    dupls = 0
    seen = set()

    for val in a:
        if val not in seen:
            seen.add(val)
            uniq += 1
        else:
            dupls += 1

    print(uniq if dupls & 1 == 0 else uniq - 1)
