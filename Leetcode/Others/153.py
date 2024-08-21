class Solution:
    def findMin(self, nums: list[int]) -> int:
        n: int = len(nums)
        left: int = 0
        right: int = n - 1

        while left < right:
            mid: int = (left + right) // 2
            el: int = nums[mid]

            if el > nums[right]:
                left = mid + 1
            else:
                right = mid

        return nums[left]
