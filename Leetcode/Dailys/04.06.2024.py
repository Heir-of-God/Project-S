class Solution:
    def longestPalindrome(self, s: str) -> int:
        char_count: dict[str, int] = {}  # up to 52 chars -> O(1) space
        for char in s:
            if char not in char_count:
                char_count[char] = 0
            char_count[char] += 1

        res = 0
        add_odd = False
        for val in char_count.values():
            res += (val // 2) * 2
            if val % 2 == 1:
                add_odd = True

        return res + int(add_odd)
