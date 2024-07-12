t = int(input())

for _ in range(t):
    length, pieces = [int(i) for i in input().split()]
    cuts = [int(i) for i in input().split()]

    mx = max(cuts)
    used_max = False
    res = 0

    for num in cuts:
        if not used_max and num == mx:
            used_max = True
            continue
        res += 2 * num - 1

    print(res)
