t = int(input())

for _ in range(t):
    a, b = [int(i) for i in input().split()]
    dif = abs(a - b)
    res = dif // 10
    res += bool(dif % 10)

    print(res)
