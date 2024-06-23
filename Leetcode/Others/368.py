class Solution:
    def largestDivisibleSubset(self, nums: list[int]) -> list[int]:
        n: int = len(nums)
        nums.sort()
        dp: list[list[int]] = [[nums[ind]] for ind in range(n)]

        for ind in range(n - 2, -1, -1):
            for next_ind in range(ind + 1, n, 1):
                if nums[next_ind] % nums[ind] == 0 and len(dp[next_ind]) + 1 > len(dp[ind]):
                    dp[ind] = [nums[ind]] + dp[next_ind]

        res_ind: int = 0
        max_length: int = len(dp[0])

        for ind in range(1, n, 1):
            subs: list[int] = dp[ind]
            cur_l: int = len(subs)

            if cur_l > max_length:
                max_length = cur_l
                res_ind = ind

        return dp[res_ind]
