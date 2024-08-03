t = int(input())

for _ in range(t):
    a, b, c, d = [int(i) for i in input().split()]
    print(int(b > a) + int(c > a) + int(d > a))
