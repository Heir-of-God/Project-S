stops = int(input())
res = 0
cur = 0

for _ in range(stops):
    leave, enter = map(int, input().split())
    cur -= leave
    cur += enter

    if cur > res:
        res = cur

print(res)
