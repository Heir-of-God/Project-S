import heapq


class Solution:
    def mincostToHireWorkers(self, quality: list[int], wage: list[int], k: int) -> float:
        workers: list[tuple[float, int]] = sorted(
            (float(w) / q, q) for w, q in zip(wage, quality)
        )  # [(ratio, quality), ...]
        res: float = float("inf")
        quality_sum = 0
        heap: list[int] = (
            []
        )  # heap is representing our "queue", when we have more than k workers we delete one with biggest quality so with minimum -quality

        for cur_ratio, q in workers:
            heapq.heappush(heap, -q)
            quality_sum += q
            if len(heap) > k:
                quality_sum += heapq.heappop(heap)
            if len(heap) == k:
                res = min(res, quality_sum * cur_ratio)

        return res
