# pure sliding window, O(n) memory
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        s += "1" if s[-1] == "0" else "0"
        n: int = len(s)
        changed = False
        res = 0
        left = 0

        for right in range(1, n):
            if s[right] != s[right - 1]:
                if changed:
                    start: int = left
                    left += 1
                    while not left or s[left] == s[left - 1]:
                        left += 1
                    cnt_first: int = left - start
                    cnt_second: int = right - left
                    res += min(cnt_first, cnt_second)
                changed = True

        return res


# optimization O(1) memory
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        s += "1" if s[-1] == "0" else "0"
        n: int = len(s)
        res = 0
        prev_count = 0
        cur_count = 0

        for ind in range(n - 1):
            cur_count += 1
            if s[ind] != s[ind + 1]:
                res += min(prev_count, cur_count)
                prev_count = cur_count
                cur_count = 0

        return res
