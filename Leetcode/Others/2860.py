class Solution:
    def countWays(self, nums: list[int]) -> int:
        nums.sort()
        n: int = len(nums)
        res: int = 1 + (nums[0] != 0)

        for ind in range(n - 1):
            selected: int = ind + 1
            if nums[ind] < selected and nums[ind + 1] > selected:
                res += 1

        return res
