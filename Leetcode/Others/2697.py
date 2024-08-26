class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        s = list(s)
        n: int = len(s)

        for ind in range(n // 2):
            reversed_ind: int = n - ind - 1
            if s[ind] != s[reversed_ind]:
                to_replace = min((s[ind], s[reversed_ind]))
                s[ind] = to_replace
                s[reversed_ind] = to_replace

        return "".join(s)
