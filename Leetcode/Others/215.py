import heapq


class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]


class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        heap: list[int] = []
        for n in nums:
            heapq.heappush(heap, n)
            if len(heap) > k:
                heapq.heappop(heap)

        return heap[0]
