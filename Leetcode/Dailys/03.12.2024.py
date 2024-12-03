class Solution:
    def addSpaces(self, s: str, spaces: list[int]) -> str:
        res: list[str] = []
        spaces = set(spaces)
        for ind, char in enumerate(s):
            if ind in spaces:
                res.append(" ")
            res.append(char)

        return "".join(res)
