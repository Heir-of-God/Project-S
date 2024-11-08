t = int(input())

for _ in range(t):
    n, k = [int(i) for i in input().split()]
    s = input()
    res = 0
    start_ind = -1

    for ind in range(n):
        if s[ind] == "B" and (start_ind == -1 or start_ind + k <= ind):
            start_ind = ind
            res += 1

    print(res)
