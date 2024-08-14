t = int(input())

for _ in range(t):
    n = int(input())
    points = [int(i) for i in input().split()]
    chars = list(input())

    rights = []
    lefts = []
    cur_s = 0

    for ind in range(n):
        p = points[ind]
        c = chars[ind]
        cur_s += p

        if c == "L":
            lefts.append((ind, cur_s - p))
        else:
            rights.append((ind, cur_s))
    lefts.reverse()

    res = 0
    while lefts and rights:
        li, l = lefts.pop()
        ri, r = rights[-1]

        if li < ri:
            rights.pop()
            res += r - l

    print(res)
