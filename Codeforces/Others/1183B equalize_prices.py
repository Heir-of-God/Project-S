q = int(input())

for _ in range(q):
    n, k = [int(i) for i in input().split()]
    arr = [int(i) for i in input().split()]
    mn = min(arr)
    mx = max(arr)
    possible_equal = mn + k

    if abs(possible_equal - mx) <= k:
        print(possible_equal)
    else:
        print(-1)
