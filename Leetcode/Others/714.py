class Solution:
    def maxProfit(self, prices: list[int], fee: int) -> int:
        n: int = len(prices)
        next_day: list[int] = [0, 0]  # have stock || don't have stock

        for ind in range(n - 1, -1, -1):
            cur_price: int = prices[ind]
            cur_day: list[int] = [0, 0]

            cur_day[0] = max(next_day[1] + cur_price - fee, next_day[0])
            cur_day[1] = max(next_day[0] - cur_price, next_day[1])
            next_day = cur_day

        return next_day[1]
