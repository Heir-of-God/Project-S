from collections import defaultdict


class Solution:
    def minimumPushes(self, word: str) -> int:
        counter = defaultdict(int)

        for char in word:
            counter[char] += 1

        res = 0
        for num, count in enumerate(sorted(counter.values(), reverse=True)):
            res += count * (num // 8 + 1)

        return res
