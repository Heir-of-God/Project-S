t = int(input())

dp = [[0, 0] for _ in range(2 * 10**5 + 1)]
dp[1] = [1, 1]
dp[2] = [1, 2]
dp[3] = [2, 4]


for number in range(4, 2 * 10**5 + 1):
    calc = 0
    n = number
    while n > 0:
        calc += 1
        n //= 3
    dp[number][0] = calc
    dp[number][1] = calc + dp[number - 1][1]

for _ in range(t):
    l, r = [int(i) for i in input().split()]
    res = dp[l][0] * 2 + dp[r][1] - dp[l][1]
    print(res)
