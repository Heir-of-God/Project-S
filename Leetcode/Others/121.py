class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n: int = len(prices)
        min_to_buy: int = prices[0]
        max_to_sell: int = 0
        res: int = 0
        prices.append(-1)

        for ind in range(1, n + 1):
            price = prices[ind]
            if price < min_to_buy:
                res = max(res, max_to_sell - min_to_buy)
                min_to_buy = price
                max_to_sell = 0
            else:
                max_to_sell = max(max_to_sell, price)

        return res
