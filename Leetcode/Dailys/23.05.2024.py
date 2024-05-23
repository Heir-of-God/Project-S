from collections import defaultdict


class Solution:
    def beautifulSubsets(self, nums: list[int], k: int) -> int:
        nums.sort()
        n: int = len(nums)
        res: int = 0

        def recursion(cur_ind, seen) -> None:
            nonlocal res

            if cur_ind == n:
                res += 1
                return

            cur_el: int = nums[cur_ind]
            if not cur_el - k in seen:
                seen[cur_el] += 1
                recursion(cur_ind + 1, seen)
                seen[cur_el] -= 1
                if not seen[cur_el]:
                    del seen[cur_el]

            recursion(cur_ind + 1, seen)

        recursion(0, defaultdict(int))
        return res - 1
