class Solution:
    def longestArithSeqLength(self, nums: list[int]) -> int:
        n: int = len(nums)
        dp: list[dict[int, int]] = [{} for _ in range(n)]
        res: int = 2

        for end_ind in range(n):
            for prev_ind in range(end_ind):
                cur_dif: int = nums[end_ind] - nums[prev_ind]
                dp[end_ind][cur_dif] = dp[prev_ind].get(cur_dif, 1) + 1
                res = max(res, dp[end_ind][cur_dif])

        return res
