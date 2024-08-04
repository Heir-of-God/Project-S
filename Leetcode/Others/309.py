class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n: int = len(prices)

        memo: list[list[int]] = [[-1, -1] for _ in range(n)]

        def recursion(day_ind: int, have_stock: bool) -> int:
            if day_ind >= n:
                return 0

            if memo[day_ind][have_stock] != -1:
                return memo[day_ind][have_stock]

            cur_price: int = prices[day_ind]
            buying: int = 0
            selling: int = 0
            do_nothing: int = recursion(day_ind + 1, have_stock)  # do nothing on this day

            if not have_stock:
                buying = recursion(day_ind + 1, True) - cur_price  # buy on this day if we can
            else:
                selling = recursion(day_ind + 2, False) + cur_price  # sell on this day if we can

            res: int = max(buying, selling, do_nothing)
            memo[day_ind][have_stock] = res
            return res

        return recursion(0, False)


# my code above was used to create this iterative solution with O(1) memory (really proud of it)


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n: int = len(prices)
        next_next_day: list[int] = [0, 0]
        next_day: list[int] = [0, 0]

        for ind in range(n - 1, -1, -1):
            cur_price = prices[ind]
            cur_day: list[int] = [0, 0]

            for have_stock in range(2):
                buying: int = 0
                selling: int = 0
                do_nothing: int = next_day[have_stock]  # do nothing on this day

                if not have_stock:
                    buying = next_day[1] - cur_price  # buy on this day if we can
                else:
                    selling = next_next_day[0] + cur_price  # sell on this day if we can

                res: int = max(buying, selling, do_nothing)
                cur_day[have_stock] = res

            next_next_day, next_day = next_day, cur_day

        return next_day[0]
