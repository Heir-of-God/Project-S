t = int(input())

for _ in range(t):
    n, m = [int(i) for i in input().split()]

    print("YES" if n >= m and n & 1 == m & 1 else "NO")
