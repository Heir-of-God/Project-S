class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n: int = len(prices)
        nxt_have_stock: list[int] = [0, 0]  # 0 transactions on this day, 1 and 2
        nxt_no_stock: list[int] = [0, 0, 0]  # 0 transactions on this day, 1 and 2

        for ind in range(n - 1, -1, -1):
            cur_price: int = prices[ind]
            cur_have: list[int] = [0, 0]
            cur_not_have: list[int] = [0, 0, 0]

            cur_have[0] = max(nxt_have_stock[0], nxt_no_stock[1] + cur_price)
            cur_have[1] = max(nxt_have_stock[1], nxt_no_stock[2] + cur_price)

            cur_not_have[0] = max(nxt_have_stock[0] - cur_price, nxt_no_stock[0])
            cur_not_have[1] = max(nxt_have_stock[1] - cur_price, nxt_no_stock[1])
            cur_not_have[2] = nxt_no_stock[2]

            nxt_have_stock = cur_have
            nxt_no_stock = cur_not_have

        return nxt_no_stock[0]
