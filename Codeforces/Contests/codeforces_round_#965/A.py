t = int(input())

for _ in range(t):
    xc, yc, k = [int(i) for i in input().split()]
    sum_x = xc * k
    sum_y = yc * k
    res = []

    res.append((sum_x, sum_y))
    if k & 1 == 1:
        cur = 1
        while len(res) != k:
            if (cur, -cur) not in res and (-cur, cur) not in res:
                res.append((cur, -cur))
                res.append((-cur, cur))
            cur += 1
    else:
        if sum_x == 0 and sum_y == 0:
            res = []
            cur = 1
            while len(res) != k:
                if (cur, -cur) not in res and (-cur, cur) not in res:
                    res.append((cur, -cur))
                    res.append((-cur, cur))
                cur += 1
        else:
            res.append((0, 0))
            cur = 1
            while len(res) != k:
                if (cur, -cur) not in res and (-cur, cur) not in res:
                    res.append((cur, -cur))
                    res.append((-cur, cur))
                cur += 1

    for point in res:
        print(point[0], point[1])
