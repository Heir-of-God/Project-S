t = int(input())

for _ in range(t):
    n = int(input())
    dig = n % 10

    res = 10 * (dig - 1)
    length = 0
    while n > 0:
        length += 1
        n //= 10

    print(res + (length + 1) * (length) // 2)
