n, m = [int(i) for i in input().split()]


def is_prime(n):
    if n == 2:
        return True
    for num in range(2, int(n**0.5) + 1, 1):
        if n % num == 0:
            return False
    return True


res = True
if is_prime(m):
    for num in range(n + 1, m, 1):
        if is_prime(num):
            res = False
            break
else:
    res = False


print("YES" if res else "NO")
