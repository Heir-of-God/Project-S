class Solution:
    def minimumMountainRemovals(self, nums: list[int]) -> int:
        n: int = len(nums)

        lis_dp: list[int] = [1 for _ in range(n)]
        lds_dp: list[int] = [1 for _ in range(n)]

        for ind in range(n):
            for prev_ind in range(ind):
                if nums[ind] > nums[prev_ind]:
                    lis_dp[ind] = max(lis_dp[ind], lis_dp[prev_ind] + 1)

        for ind in range(n - 1, -1, -1):
            for prev_ind in range(ind + 1, n):
                if nums[ind] > nums[prev_ind]:
                    lds_dp[ind] = max(lds_dp[ind], lds_dp[prev_ind] + 1)

        res = float("inf")
        for ind in range(n):
            if lis_dp[ind] > 1 and lds_dp[ind] > 1:
                res = min(res, n - lis_dp[ind] - lds_dp[ind] + 1)  # you "remove" peak twice so + 1

        return res
