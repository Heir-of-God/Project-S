class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        res = 0
        for num in nums:
            if not num % 3 == 0:
                res += 1
        return res
