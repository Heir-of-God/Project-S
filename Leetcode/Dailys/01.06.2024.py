class Solution:
    def scoreOfString(self, s: str) -> int:
        res: int = 0
        n: int = len(s)
        for first_ind in range(n - 1):
            res += abs(ord(s[first_ind]) - ord(s[first_ind + 1]))

        return res
