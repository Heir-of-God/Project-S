t = int(input())

for _ in range(t):
    n = int(input())
    div = n % 7
    add = 7 - div
    last_digit = n % 10

    if last_digit >= div:
        n -= div
    else:
        n += add

    print(n)
