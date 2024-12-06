t = int(input())

for _ in range(t):
    x = abs(int(input()))
    if x % 3 == 0:
        print(x // 3)
    elif x in [-1, 1]:
        print(2)
    else:
        print(x // 3 + 1)
