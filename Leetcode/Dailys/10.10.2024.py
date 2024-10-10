class Solution:
    def maxWidthRamp(self, nums: list[int]) -> int:
        n: int = len(nums)
        max_to_right: list[int] = [0 for _ in range(n)]
        cur_mx = -1

        for ind in range(n - 1, -1, -1):
            if nums[ind] > cur_mx:
                cur_mx = nums[ind]
            max_to_right[ind] = cur_mx

        res = 0
        left = 0
        for right in range(1, n):
            while nums[left] > max_to_right[right]:
                left += 1
            res = max(res, right - left)

        return res
