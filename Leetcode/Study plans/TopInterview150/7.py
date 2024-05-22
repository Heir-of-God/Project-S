class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        cur_max = 0
        cur_minimum_to_buy: int = prices[0]
        n: int = len(prices)

        for ind in range(1, n):
            local_max: int = prices[ind] - cur_minimum_to_buy
            if local_max > cur_max:
                cur_max: int = local_max
            if cur_minimum_to_buy > prices[ind]:
                cur_minimum_to_buy = prices[ind]

        return cur_max
