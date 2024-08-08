class Solution:
    def knightDialer(self, n: int) -> int:
        MOD = 10**9 + 7
        prev_dp: list[int] = [1 for _ in range(10)]  # prev_dp[i] - number of numbers which ends on i

        for _ in range(n - 1):
            cur_dp: list[int] = [0 for _ in range(10)]
            cur_dp[0] = prev_dp[4] + prev_dp[6]
            cur_dp[1] = prev_dp[8] + prev_dp[6]
            cur_dp[2] = prev_dp[7] + prev_dp[9]
            cur_dp[3] = prev_dp[4] + prev_dp[8]
            cur_dp[4] = prev_dp[3] + prev_dp[9] + prev_dp[0]
            cur_dp[5] = 0
            cur_dp[6] = prev_dp[1] + prev_dp[7] + prev_dp[0]
            cur_dp[7] = prev_dp[2] + prev_dp[6]
            cur_dp[8] = prev_dp[1] + prev_dp[3]
            cur_dp[9] = prev_dp[4] + prev_dp[2]
            prev_dp = [val % MOD for val in cur_dp]

        return sum(prev_dp) % MOD
