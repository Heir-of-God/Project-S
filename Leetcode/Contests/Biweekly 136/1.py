class Solution:
    def winningPlayerCount(self, n: int, pick: list[list[int]]) -> int:
        counting: list[list[int]] = [[0 for _ in range(12)] for _ in range(n)]

        for player, color in pick:
            counting[player][color] += 1

        res = 0
        for ind, player in enumerate(counting):
            for color in player:
                if color > ind:
                    res += 1
                    break

        return res
