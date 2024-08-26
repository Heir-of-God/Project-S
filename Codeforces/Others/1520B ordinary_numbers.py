t = int(input())


def get_length(n):
    res = 0
    while n > 0:
        n //= 10
        res += 1

    return res


def get_first(l):
    res = 0
    for _ in range(l):
        res *= 10
        res += 1
    return res


for _ in range(t):
    n = int(input())
    length = get_length(n)
    res = 9 * (length - 1)
    first = get_first(length)

    for i in range(1, 10):
        if first * i <= n:
            res += 1
        else:
            break
    print(res)
