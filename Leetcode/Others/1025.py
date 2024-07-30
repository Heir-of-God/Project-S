class Solution:
    def divisorGame(self, n: int) -> bool:
        dp: list[bool] = [
            False for _ in range(n + 1)
        ]  # who end up with num dp[num] win if dp[num] is True and lose otherwise

        for num in range(2, n + 1, 1):
            for possible_divisor in range(1, num, 1):
                if num % possible_divisor == 0:
                    if dp[num - possible_divisor] == False:
                        dp[num] = True
                        break
        return dp[n]


class Solution:
    def divisorGame(self, n: int) -> bool:
        return not n % 2
