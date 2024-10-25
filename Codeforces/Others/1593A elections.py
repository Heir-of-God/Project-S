t = int(input())

for _ in range(t):
    a, b, c = [int(i) for i in input().split()]
    print(max(max(b, c) - a + 1, 0), max(max(a, c) - b + 1, 0), max(max(b, a) - c + 1, 0))
