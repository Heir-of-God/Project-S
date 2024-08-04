class Solution:
    def countBits(self, n: int) -> list[int]:
        dp: list[int] = [0 for _ in range(n + 1)]

        for num in range(1, n + 1, 1):
            last_bit: int = num & 1
            num_from_other_bits: int = num >> 1  # this num is always < num and we already counted 1 for it
            dp[num] = last_bit + dp[num_from_other_bits]

        return dp
