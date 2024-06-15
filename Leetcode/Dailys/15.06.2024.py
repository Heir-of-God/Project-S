import heapq


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: list[int], capital: list[int]) -> int:
        minimum_capital: list[tuple[int, int]] = list(zip(capital, profits))
        maximum_profit: list[int] = []
        heapq.heapify(minimum_capital)
        cur_capital: int = w

        for _ in range(k):
            while minimum_capital and minimum_capital[0][0] <= cur_capital:
                project_profit: int = heapq.heappop(minimum_capital)[1]
                heapq.heappush(maximum_profit, -project_profit)

            if not maximum_profit:
                return cur_capital
            cur_capital += -(heapq.heappop(maximum_profit))

        return cur_capital
