t = int(input())

for _ in range(t):
    n = int(input())
    arr = [int(i) for i in input().split()]
    res_stack = [0 for _ in range(n)]
    cream = 0

    for ind in range(n - 1, -1, -1):
        cream = max(cream, arr[ind])
        if cream:
            res_stack[ind] = 1
            cream -= 1

    print(" ".join([str(i) for i in res_stack]))
