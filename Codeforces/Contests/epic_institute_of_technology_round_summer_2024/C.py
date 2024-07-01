t = int(input())


def find_seconds(n, arr):
    res = 0
    for ind in range(n):
        res = max(res, arr[ind] + ind)
    return res


for _ in range(t):
    n = int(input())
    a = [int(ind) for ind in input().split()]
    print(find_seconds(n, a))
