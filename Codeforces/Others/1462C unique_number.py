t = int(input())

for _ in range(t):
    x = int(input())
    if x > 45:
        print(-1)
        continue

    res = 0
    added = 0
    cur_dig = 9

    while cur_dig != 0 and x != 0:
        if cur_dig <= x:
            x -= cur_dig
            res = cur_dig * 10**added + res
            added += 1
        cur_dig -= 1

    print(-1 if x != 0 else res)
