t = int(input())

for _ in range(t):
    a, b = [int(i) for i in input().split()]

    if (a + b) & 1 == 1:
        print("Alice")
    else:
        print("Bob")
