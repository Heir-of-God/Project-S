t = int(input())

for _ in range(t):
    xs = [int(i) for i in input().split()]
    xs.sort()

    print(xs[2] - xs[0])
