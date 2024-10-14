from heapq import heapify, heappop, heappush
from math import ceil


class Solution:
    def maxKelements(self, nums: list[int], k: int) -> int:
        nums = [-num for num in nums]
        heapify(nums)
        res = 0

        for _ in range(k):
            num: int = -heappop(nums)
            res += num
            heappush(nums, -ceil(num / 3))

        return res
