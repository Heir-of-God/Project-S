t = int(input())

for _ in range(t):
    h, m = [int(i) for i in input().split()]
    print(24 * 60 - h * 60 - m)
