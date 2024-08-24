t = int(input())

for _ in range(t):
    n = int(input())
    arr = input().split()
    cur = 0
    res = 0
    arr.append("1")

    for el in arr:
        if el == "0":
            cur += 1
        else:
            res = max(res, cur)
            cur = 0

    print(res)
