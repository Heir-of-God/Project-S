t = int(input())
for _ in range(t):
    a, b, c = [int(i) for i in input().split()]
    second = 2 * c - b if c > b else b

    print(1 if a < second else 2 if second < a else 3)
