class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        n: int = len(s)
        cur_cost: int = 0
        left: int = 0
        res: int = 0

        for right in range(n):
            cur_cost += abs(ord(t[right]) - ord(s[right]))
            while cur_cost > maxCost:
                cur_cost -= abs(ord(t[left]) - ord(s[left]))
                left += 1
            res = max(res, right - left + 1)

        return res
