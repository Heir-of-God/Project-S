class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        prev_prev: int = 0
        prev: int = 0

        for price in cost:
            price_from_here: int = min(prev_prev, prev) + price  # the minimum price to go from this step
            prev_prev = prev
            prev = price_from_here

        return min(prev_prev, prev)
