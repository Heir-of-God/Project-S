class Solution:
    def shortestPalindrome(self, s: str) -> str:
        left, n = 0, len(s)
        for c in s[::-1]:
            if c == s[left]:
                left += 1
        if left == n:
            return s
        sub = s[left:]
        return sub[::-1] + self.shortestPalindrome(s[0:left]) + sub
