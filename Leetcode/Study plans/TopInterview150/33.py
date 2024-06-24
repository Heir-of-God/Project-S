from collections import defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        needed_count = defaultdict(int)
        for char in t:
            needed_count[char] += 1
        needed_length: int = len(t)
        res: tuple[int, int] = (0, float("inf"))  # representing start and right of the shortest substring

        left = 0
        for right, char in enumerate(s):
            if needed_count[char] > 0:
                needed_length -= 1
            needed_count[char] -= 1
            if needed_length == 0:
                while True:
                    left_char: str = s[left]
                    if (
                        needed_count[left_char] == 0
                    ):  # if we reached the first symbol which is present in t (all others are negative so far)
                        print(needed_count)
                        break
                    needed_count[left_char] += 1
                    left += 1
                if right - left < res[1] - res[0]:
                    res = (left, right)
                needed_count[s[left]] += 1
                needed_length += 1
                left += 1
        return "" if res[1] > len(s) else s[res[0] : res[1] + 1]
