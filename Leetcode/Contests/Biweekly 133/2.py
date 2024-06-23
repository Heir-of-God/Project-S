class Solution:
    def minOperations(self, nums: list[int]) -> int:
        n: int = len(nums)
        res = 0

        for ind in range(n - 2):
            if nums[ind] == 0:
                nums[ind] = 1 - nums[ind]
                nums[ind + 1] = 1 - nums[ind + 1]
                nums[ind + 2] = 1 - nums[ind + 2]
                res += 1

        for ind in range(n):
            if nums[ind] == 0:
                return -1

        return res
