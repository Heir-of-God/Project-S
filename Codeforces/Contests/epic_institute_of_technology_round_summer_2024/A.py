t = int(input())

for _ in range(t):
    n, k = input().split()
    n = int(n)
    k = int(k)
    print(k * (n - 1) + 1)
