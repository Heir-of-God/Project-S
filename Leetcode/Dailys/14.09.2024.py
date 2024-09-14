class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        mx: int = max(nums)
        res: int = 1
        cur: int = 0
        nums.append(mx - 1)

        for num in nums:
            if num == mx:
                cur += 1
            else:
                res = max(res, cur)
                cur = 0

        return res
