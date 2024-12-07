t = int(input())

for _ in range(t):
    n = int(input())
    a = [int(i) for i in input().split()]
    s = sum(a)

    if s % 3 == 0:
        print(0)
        continue
    elif s % 3 == 2:
        print(1)
        continue

    f = False
    for val in a:
        if val % 3 == s % 3:
            f = True
            break

    print(1 if f else 2)
