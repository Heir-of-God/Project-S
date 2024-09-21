t = int(input())

for _ in range(t):
    a, b = [int(i) for i in input().split()]
    if a == b:
        print(0)
    elif (a > b and a % 2 == b % 2) or (b % 2 != a % 2 and a < b):
        print(1)
    else:
        print(2)
