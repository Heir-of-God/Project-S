t = int(input())

for _ in range(t):
    x, k = [int(i) for i in input().split()]

    if x % k != 0:
        print(1)
        print(x)
    else:
        print(2)
        print(x - 1, 1)
