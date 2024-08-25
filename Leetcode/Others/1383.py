from heapq import heappop, heappush


class Solution:
    def maxPerformance(self, n: int, speed: list[int], efficiency: list[int], k: int) -> int:
        MOD = 10**9 + 7
        engineers: list[tuple[int, int]] = sorted(zip(efficiency, speed), reverse=True)
        speed_heap: list[int] = []
        speed_sum: int = 0
        res: int = 0

        for ef, sp in engineers:
            removed: int = -1
            if len(speed_heap) == k:
                removed = heappop(speed_heap)
                speed_sum -= removed

            heappush(speed_heap, sp)
            speed_sum += sp
            res = max(res, speed_sum * ef)

            if removed != -1 and removed > sp:
                heappop(speed_heap)
                speed_sum -= sp
                speed_sum += removed
                heappush(speed_heap, removed)

        return res % MOD
