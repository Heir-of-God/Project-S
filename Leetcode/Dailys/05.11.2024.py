class Solution:
    def minChanges(self, s: str) -> int:
        res: int = 0
        for ind in range(1, len(s), 2):
            if s[ind] != s[ind - 1]:
                res += 1

        return res
