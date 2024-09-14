t = int(input())

for _ in range(t):
    coords = [[int(i) for i in input().split()] for _ in range(4)]
    if coords[0][1] != coords[1][1]:
        print((coords[1][1] - coords[0][1]) ** 2)
    elif coords[0][1] != coords[2][1]:
        print((coords[2][1] - coords[0][1]) ** 2)
