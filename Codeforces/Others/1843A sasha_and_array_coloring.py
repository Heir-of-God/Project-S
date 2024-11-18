t = int(input())

for _ in range(t):
    n = int(input())
    arr = [int(i) for i in input().split()]
    arr.sort()
    res = 0

    for left in range(n // 2):
        res += arr[n - left - 1] - arr[left]

    print(res)
