class Solution:
    def numSquares(self, n: int) -> int:
        if n**0.5 == int(n**0.5):
            return 1
        squares: list[int] = []
        cur = 1
        while cur**2 <= n:
            squares.append(cur**2)
            cur += 1

        dp: list[int] = [float("inf") for _ in range(n + 1)]
        dp[0] = 0

        for number in range(1, n + 1, 1):
            for square in squares:
                if square > n:
                    break
                dp[number] = min(dp[number], dp[number - square] + 1)

        return dp[n]
