from collections import deque


class Solution:
    def shortestSubarray(self, nums: list[int], k: int) -> int:
        res: int = float("inf")
        deq: deque[tuple[int, int]] = deque([(0, -1)])  # (prefix_sum, prefix_end_ind)
        cur_sum: int = 0

        for ind, val in enumerate(nums):
            cur_sum += val

            while deq and cur_sum - deq[0][0] >= k:
                res = min(res, ind - deq.popleft()[1])

            while deq and deq[-1][0] >= cur_sum:
                deq.pop()

            deq.append((cur_sum, ind))

        return res if res != float("inf") else -1
