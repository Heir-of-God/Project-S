class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        res: int = nums[0]
        cur_sum: int = 0
        nums.append(-float("inf"))

        for num in nums:
            cur_sum += num
            res = max(res, cur_sum)
            if cur_sum < 0:
                cur_sum = 0

        return res
