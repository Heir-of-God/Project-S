class Solution:
    def search(self, nums: list[int], target: int) -> int:
        n: int = len(nums)
        left: int = 0
        right: int = n - 1

        while left <= right:
            mid: int = (left + right) // 2
            cur_num: int = nums[mid]

            if cur_num < target:
                left = mid + 1
            elif cur_num > target:
                right = mid - 1
            else:
                return mid

        return -1
