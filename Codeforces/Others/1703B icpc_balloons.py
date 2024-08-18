t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    seen = set()
    res = 0

    for p in s:
        if p not in seen:
            seen.add(p)
            res += 1
        res += 1

    print(res)
