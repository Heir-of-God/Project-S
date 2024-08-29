class Solution:
    def minimumMoves(self, s: str) -> int:
        res: int = 0
        left: int = -1
        s += "000"

        for ind, char in enumerate(s):
            if left != -1 and ind - left == 3:
                res += 1
                left = -1

            if left == -1 and char == "X":
                left = ind

        return res
