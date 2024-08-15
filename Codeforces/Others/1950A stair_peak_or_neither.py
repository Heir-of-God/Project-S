t = int(input())

for _ in range(t):
    a, b, c = [int(i) for i in input().split()]

    if a < b < c:
        print("STAIR")
    elif b > a and b > c:
        print("PEAK")
    else:
        print("NONE")
