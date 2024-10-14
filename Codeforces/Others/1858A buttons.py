t = int(input())

for _ in range(t):
    a, b, c = [int(i) for i in input().split()]
    print("First" if (c % 2 == 0 and a > b) or (c % 2 == 1 and a >= b) else "Second")
