t = int(input())

for _ in range(t):
    a, b, c = [int(i) for i in input().split()]

    if a < b < c or c < b < a:
        print(b)
    elif b < a < c or c < a < b:
        print(a)
    else:
        print(c)
