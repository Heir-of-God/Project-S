class Solution:
    def maxEqualRowsAfterFlips(self, matrix: list[list[int]]) -> int:
        count: dict[str, int] = {}

        for row in matrix:
            res: str = ""
            prev = -1
            for val in row:
                if val != prev:
                    prev = val
                    res += "|"
                res += "*"
            if not res in count:
                count[res] = 0
            count[res] += 1

        return max(count.values())
