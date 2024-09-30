t = int(input())

for _ in range(t):
    n = int(input())
    four = n // 4
    two = (n - four * 4) // 2

    print(two + four)
