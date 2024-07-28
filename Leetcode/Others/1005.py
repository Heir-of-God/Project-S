class Solution:
    def largestSumAfterKNegations(self, nums: list[int], k: int) -> int:
        nums.sort()
        res: int = 0
        mn_abs: int = 101
        for num in nums:
            add: int = num
            if k > 0 and num < 0:
                k -= 1
                add *= -1
            elif num == 0:
                k = 0
            mn_abs = min(abs(num), mn_abs)
            res += add

        return res if k & 1 == 0 else res - 2 * mn_abs
