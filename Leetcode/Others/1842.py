class Solution:
    def getMinDistance(self, nums: list[int], target: int, start: int) -> int:
        n: int = len(nums)
        res = 0
        while True:
            left: int = nums[start - res] if 0 <= start - res < n else 0
            right: int = nums[start + res] if 0 <= start + res < n else 0
            if target in (left, right):
                return res
            res += 1
