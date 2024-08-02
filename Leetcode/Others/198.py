class Solution:
    def rob(self, nums: list[int]) -> int:
        n: int = len(nums)
        dp: list[int] = [0 for _ in range(n + 1)]  # dp[i] - maximum amount of money you can get from first i houses
        dp[1] = nums[0]

        for number_of_houses in range(2, n + 1, 1):
            house_ind: int = number_of_houses - 1
            dp[number_of_houses] = max(dp[number_of_houses - 1], dp[number_of_houses - 2] + nums[house_ind])

        return dp[n]
