MOD = 10**9 + 7


def combinations(n, k, factorial, inv_factorial):
    if k > n or k < 0:
        return 0
    return (factorial[n] * inv_factorial[k] % MOD) * inv_factorial[n - k] % MOD


def get_factorials(max_n):
    factorial = [1] * (max_n + 1)
    inv_factorial = [1] * (max_n + 1)

    for i in range(2, max_n + 1):
        factorial[i] = factorial[i - 1] * i % MOD

    inv_factorial[max_n] = pow(factorial[max_n], MOD - 2, MOD)

    for i in range(max_n - 1, 0, -1):
        inv_factorial[i] = inv_factorial[i + 1] * (i + 1) % MOD

    return factorial, inv_factorial


factorial, inv_factorial = get_factorials(2 * 10**5)


t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    ones_count = sum(arr)
    min_ones = (k + 1) // 2

    if ones_count < min_ones:
        print(0)
        continue

    res = 0
    for number_of_ones in range(min_ones, ones_count + 1):
        choose1 = combinations(ones_count, number_of_ones, factorial, inv_factorial)
        choose0 = combinations(n - ones_count, k - number_of_ones, factorial, inv_factorial)
        res += choose1 * choose0 % MOD
        res %= MOD

    print(res)
