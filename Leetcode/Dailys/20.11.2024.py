from typing import Counter


class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        if k == 0:
            return 0
        cur = Counter(s)
        for val in cur.values():
            if val < k or len(cur) < 3:
                return -1
        res: int = float("inf")
        left: int = 0

        for right in range(len(s)):
            cur[s[right]] -= 1

            while cur[s[right]] < k:
                cur[s[left]] += 1
                left += 1

            res = min(res, len(s) - (right - left + 1))

        return res
