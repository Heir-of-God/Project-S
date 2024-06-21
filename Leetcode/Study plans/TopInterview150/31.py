class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n: int = len(s)
        res: int = 0
        left: int = 0
        seen: int = set()

        for right in range(0, n, 1):
            cur_char: str = s[right]
            if cur_char in seen:
                res = max(res, right - left)
                while s[left] != cur_char:
                    seen.remove(s[left])
                    left += 1
                left += 1
            else:
                seen.add(cur_char)

        res = max(res, n - left)
        return res
