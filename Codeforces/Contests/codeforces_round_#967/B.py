t = int(input())

for _ in range(t):
    n = int(input())
    if n & 1 == 0:
        print(-1)
    else:
        cur_ind = 0
        c = 1
        res = [0 for _ in range(n)]
        while cur_ind < n // 2:
            right = n - cur_ind - 1
            res[right] = c
            res[cur_ind] = c + 1
            c += 2
            cur_ind += 1
        res[n // 2] = c

        print(" ".join([str(i) for i in res]))
