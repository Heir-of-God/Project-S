class Solution:
    def integerBreak(self, n: int) -> int:
        dp: list[int] = [0 for _ in range(n + 1)]
        dp[2] = 1

        for num in range(3, n + 1, 1):
            for first_num in range(1, num // 2 + 2, 1):
                second_num: int = num - first_num
                dp[num] = max(
                    dp[num],
                    first_num * second_num,
                    dp[first_num] * second_num,
                    first_num * dp[second_num],
                    dp[first_num] * dp[second_num],
                )
                # maximum from itself, product of two raw nums and different ways involving breaking any of this two numbers

        return dp[n]
