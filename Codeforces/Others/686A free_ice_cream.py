n, x = [int(i) for i in input().split()]
queue = [int(input().replace(" ", "")) for _ in range(n)]
res = 0

for p in queue:
    if p > 0:
        x += p
    else:
        if -p > x:
            res += 1
        else:
            x += p

print(x, res)
