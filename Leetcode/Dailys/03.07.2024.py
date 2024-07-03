import heapq


class Solution:
    def minDifference(self, nums: list[int]) -> int:
        if len(nums) <= 4:
            return 0
        nums.sort()
        return min(
            nums[-4] - nums[0],
            nums[-1] - nums[3],
            nums[-3] - nums[1],
            nums[-2] - nums[2],
        )


class Solution:
    def minDifference(self, nums: list[int]) -> int:
        n: int = len(nums)
        if n <= 4:
            return 0
        elif n < 8:
            nums.sort()
        else:
            nums = sorted(heapq.nsmallest(4, nums)) + sorted(heapq.nlargest(4, nums))

        return min(
            nums[-4] - nums[0],
            nums[-1] - nums[3],
            nums[-3] - nums[1],
            nums[-2] - nums[2],
        )
