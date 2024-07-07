num = int(input())


def count_lucky_digits(num):
    res = 0
    while num > 0:
        dig = num % 10
        num //= 10
        if dig in [4, 7]:
            res += 1
    return res


def count_digits(num):
    if num == 0:
        return 1
    res = 0
    while num > 0:
        res += 1
        num //= 10
    return res


lucky_here = count_lucky_digits(num)
print("YES" if count_lucky_digits(lucky_here) == count_digits(lucky_here) else "NO")
