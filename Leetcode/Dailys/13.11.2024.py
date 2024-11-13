class Solution:
    def countFairPairs(self, nums, lower, upper) -> int:
        nums.sort()
        res: int = 0

        def first_not_smaller(nums, low, val):
            high: int = len(nums) - 1
            while low <= high:
                mid = low + ((high - low) // 2)
                if nums[mid] >= val:
                    high = mid - 1
                else:
                    low = mid + 1
            return low

        for ind in range(len(nums)):
            low: int = first_not_smaller(nums, ind + 1, lower - nums[ind])
            high: int = first_not_smaller(nums, ind + 1, upper - nums[ind] + 1)
            res += high - low

        return res
