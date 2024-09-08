t = int(input())

for _ in range(t):
    n, k = [int(i) for i in input().split()]
    arr = [int(i) for i in input().split()]
    print("YES" if k in arr else "NO")
