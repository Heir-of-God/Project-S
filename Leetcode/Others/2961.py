class Solution:
    def getGoodIndices(self, variables: list[list[int]], target: int) -> list[int]:
        res: list[int] = []

        for ind, variable in enumerate(variables):
            a, b, c, m = variable
            if target < m:
                a %= 10
                inbrackets = ((a**b) % 10) % m
                if (inbrackets**c) % m == target:
                    res.append(ind)

        return res
