class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        res = 0
        opened = 0

        for char in s:
            if char == "(":
                opened += 1
            elif char == ")":
                if not opened:
                    res += 1
                else:
                    opened -= 1

        return res + opened
