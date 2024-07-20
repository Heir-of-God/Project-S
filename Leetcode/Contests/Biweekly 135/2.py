class Solution:
    def minimumLength(self, s: str) -> int:
        res: int = len(s)
        counter: dict[str, int] = {}

        for char in s:
            if char not in counter:
                counter[char] = 0
            counter[char] += 1
            if counter[char] == 3:
                counter[char] = 1
                res -= 2

        return res
