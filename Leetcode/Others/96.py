class Solution:
    def numTrees(self, n: int) -> int:
        dp: list[int] = [0 for _ in range(n + 1)]
        dp[0] = 1
        dp[1] = 1

        for number_of_nodes in range(2, n + 1, 1):
            for possible_root in range(1, number_of_nodes + 1, 1):
                dp[number_of_nodes] += dp[possible_root - 1] * dp[number_of_nodes - possible_root]

        return dp[n]
