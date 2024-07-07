class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        res: int = numBottles
        cur_empty: int = numBottles

        while cur_empty // numExchange != 0:
            full_drinked: int = cur_empty // numExchange
            left_empty: int = cur_empty - full_drinked * numExchange
            res += full_drinked
            cur_empty = left_empty + full_drinked

        return res


class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        return numBottles + (numBottles - 1) // (numExchange - 1)
