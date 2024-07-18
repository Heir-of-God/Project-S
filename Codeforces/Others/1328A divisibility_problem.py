t = int(input())

for _ in range(t):
    a, b = [int(i) for i in input().split()]
    if a < b:
        print(b - a)
        continue

    print((b - a % b) % b)
