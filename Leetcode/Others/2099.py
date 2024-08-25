from heapq import nlargest


class Solution:
    def maxSubsequence(self, nums: list[int], k: int) -> list[int]:
        nums = [(n, i) for i, n in enumerate(nums)]
        largs: list[int] = nlargest(k, nums)
        largs.sort(key=lambda x: x[1])

        return [n[0] for n in largs]
