class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp: list[int] = [-1 for _ in range(amount + 1)]
        dp[0] = 0

        for coin in coins:
            for num in range(coin, amount + 1, 1):
                if dp[num - coin] != -1:
                    dp[num] = min(dp[num] if dp[num] != -1 else float("inf"), dp[num - coin] + 1)

        return dp[amount]
