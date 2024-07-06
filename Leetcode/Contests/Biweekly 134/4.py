from collections import defaultdict


class Solution:
    def countSubarrays(self, nums: list[int], k: int) -> int:
        n: int = len(nums)
        res: int = 0
        cache = defaultdict(int)

        for ind in range(n):
            cur = defaultdict(int)
            cur_n: int = nums[ind]
            if cur_n == k:
                res += 1
            cur[cur_n] = 1

            for val, freq in cache.items():
                after_operation = val & cur_n
                if after_operation == k:
                    res += freq
                cur[after_operation] += freq

            cache = cur

        return res
