class Solution:
    def longestSquareStreak(self, nums: list[int]) -> int:
        check = set(nums)
        res = 0

        for start in nums:
            l = 1
            cur = start

            while cur**2 in check:
                l += 1
                cur **= 2

            res = max(res, l)
            if res == 5:
                return res

        return res if res >= 2 else -1
