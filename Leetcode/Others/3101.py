class Solution:
    def countAlternatingSubarrays(self, nums: list[int]) -> int:
        n: int = len(nums)
        res: int = 0
        prev_el: int = -1
        cur_l: int = 0

        for right in range(n):
            if prev_el == nums[right]:
                cur_l = 0
            cur_l += 1
            res += cur_l
            prev_el = nums[right]

        return res
