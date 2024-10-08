class Solution:
    def minSwaps(self, s: str) -> int:
        res = 0
        opened = 0

        for char in s:
            if char == "]":
                if not opened:
                    res += 1
                    opened = 2
                opened -= 1
            elif char == "[":
                opened += 1

        return res
