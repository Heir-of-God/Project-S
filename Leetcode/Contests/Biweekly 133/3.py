class Solution:
    def minOperations(self, nums: list[int]) -> int:
        res: int = 0
        n: int = len(nums)
        is_flipped: int = 0

        for ind in range(n):
            if nums[ind] == is_flipped:
                res += 1
                is_flipped = 1 - is_flipped

        return res
