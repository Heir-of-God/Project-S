t = int(input())

for _ in range(t):
    n, k = [int(i) for i in input().split()]
    arr = [int(i) for i in input().split()]

    if k >= 2 or arr == sorted(arr):
        print("YES")
    else:
        print("NO")
