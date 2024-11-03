t = int(input())

for _ in range(t):
    n, k = [int(i) for i in input().split()]
    arr = [int(i) for i in input().split()]
    cur = 0
    res = 0

    for el in arr:
        if el >= k:
            cur += el
        elif el == 0 and cur > 0:
            cur -= 1
            res += 1

    print(res)
