from heapq import heapify, heappop, heappush


class Solution:
    def halveArray(self, nums: list[int]) -> int:
        target: float = sum(nums) / 2
        nums = [-i for i in nums]
        heapify(nums)
        res: int = 0
        cur: float = 0

        while cur < target:
            res += 1
            biggest: int = -heappop(nums)
            cur += biggest / 2
            heappush(nums, -biggest / 2)

        return res
