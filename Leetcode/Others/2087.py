class Solution:
    def minCost(self, startPos: list[int], homePos: list[int], rowCosts: list[int], colCosts: list[int]) -> int:
        res: int = 0
        for row_ind in range(min(startPos[0], homePos[0]), max(startPos[0], homePos[0]) + 1):
            res += rowCosts[row_ind]
        for col_ind in range(min(startPos[1], homePos[1]), max(startPos[1], homePos[1]) + 1):
            res += colCosts[col_ind]
        res -= rowCosts[startPos[0]]
        res -= colCosts[startPos[1]]

        return res
