class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        MOD = 10**9 + 7
        dp: list[int] = [0 for _ in range(n + 1)]  # dp[i] how many persons discovered secret after day i
        dp[1] = 1

        for day in range(2, n + 1, 1):
            for prev_day in range(max(day - forget + 1, 1), day - delay + 1, 1):
                dp[day] += dp[prev_day]
                dp[day] %= MOD

        res = 0
        for day in range(n - forget + 1, n + 1, 1):
            res += dp[day]

        return res % MOD
