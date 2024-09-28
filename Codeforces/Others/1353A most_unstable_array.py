t = int(input())

for _ in range(t):
    n, m = [int(i) for i in input().split()]

    if n == 1:
        print(0)
    elif n == 2:
        print(m)
    else:
        print(m * 2)
