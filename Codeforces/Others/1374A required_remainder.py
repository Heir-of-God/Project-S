t = int(input())

for _ in range(t):
    x, y, n = [int(i) for i in input().split()]
    cur_remainder = n % x
    n -= cur_remainder - y if cur_remainder - y >= 0 else cur_remainder + (x - y)

    print(n)
