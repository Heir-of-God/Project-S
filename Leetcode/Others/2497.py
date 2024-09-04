from heapq import heappop, heappush


class Solution:
    def maxStarSum(self, vals: list[int], edges: list[list[int]], k: int) -> int:
        def add_to_heap(val, heap) -> None:
            if val > 0:
                heappush(heap, val)
                if len(heap) > k:
                    heappop(heap)

        n: int = len(vals)
        stars: list[list[int]] = [[] for edge in range(n)]

        for edge1, edge2 in edges:
            add_to_heap(vals[edge1], stars[edge2])
            add_to_heap(vals[edge2], stars[edge1])

        res = -(10**5)
        for ind, star in enumerate(stars):
            res: int = max(res, sum(star) + vals[ind])

        return res
