class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        need: dict[str, int] = {}
        for char in target:
            if char not in need:
                need[char] = 0
            need[char] += 1

        count: dict[str, int] = {}
        for char in s:
            if char not in count and char in need:
                count[char] = 0
            if char in need:
                count[char] += 1

        if len(count) != len(need):
            return 0

        res: int = 101
        for char in need:
            if char in count:
                res = min(res, count[char] // need[char])

        return res
