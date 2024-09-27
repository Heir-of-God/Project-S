t = int(input())

for _ in range(t):
    l, r = [int(i) for i in input().split()]

    if l * 2 > r:
        print(-1, -1)
    else:
        print(l, l * 2)
