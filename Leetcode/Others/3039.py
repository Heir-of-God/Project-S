class Solution:
    def lastNonEmptyString(self, s: str) -> str:
        n: int = len(s)
        counting: list[int] = [0 for _ in range(26)]
        for char in s:
            counting[ord(char) - ord("a")] += 1
        mx: int = max(counting)
        res: str = ""
        for ind in range(n - 1, -1, -1):
            char = s[ind]
            if counting[ord(char) - ord("a")] == mx:
                res += char
                counting[ord(char) - ord("a")] -= 1

        return res[::-1]
