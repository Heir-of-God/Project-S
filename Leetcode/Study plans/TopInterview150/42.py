from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counter = defaultdict(int)

        for char in s:
            counter[char] += 1

        for char in t:
            counter[char] -= 1

        for val in counter.values():
            if val != 0:
                return False

        return True
