class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 10**9 + 7
        # 0 -> column full filled, 1 -> has missing block on top, 2 -> has missing block in bottom (for every state all previous columns are filled)
        dp: list[list[int]] = [[0, 0, 0] for _ in range(n + 1)]
        dp[0][0] = 1
        dp[1][0] = 1

        for number_of_columns in range(2, n + 1):
            # valid state - for every possible state before add new required block
            dp[number_of_columns][0] = (
                dp[number_of_columns - 1][0]  # one vertical
                + dp[number_of_columns - 2][0]  # two horizontal
                + dp[number_of_columns - 1][1]  # tromino with block on top
                + dp[number_of_columns - 1][2]  # tromino with block on bottom
            )
            # block on top is missing if we add one horizontal domino to the state where bottom block was missing or if we add tromino to valid state
            dp[number_of_columns][1] = dp[number_of_columns - 1][2] + dp[number_of_columns - 2][0]
            # the same as above but in reverse
            dp[number_of_columns][2] = dp[number_of_columns - 1][1] + dp[number_of_columns - 2][0]

        return dp[n][0] % MOD
