t = int(input())

for _ in range(t):
    n = int(input())
    arr = [int(i) for i in input().split()]
    seen = set()
    res = []

    for num in arr:
        if num not in seen:
            seen.add(num)
            res.append(num)

    print(*res)
