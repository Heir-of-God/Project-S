import heapq


class Solution:
    def rangeSum(self, nums: list[int], n: int, left: int, right: int) -> int:
        mod: int = 10**9 + 7
        res: list[int] = []

        for start_ind in range(n):
            cur_s = 0
            for end_ind in range(start_ind, n):
                cur_s += nums[end_ind]
                res.append(cur_s)

        return sum(heapq.nsmallest(right, res)[left - 1 :]) % mod
