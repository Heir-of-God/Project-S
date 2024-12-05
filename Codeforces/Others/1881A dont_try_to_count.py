t = int(input())

for _ in range(t):
    n, m = [int(i) for i in input().split()]
    x = input()
    s = input()
    found = False

    for i in range(0, 6, 1):
        if s in x:
            print(i)
            found = True
            break
        x = x * 2

    if not found:
        print(-1)
