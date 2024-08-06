class Solution:
    def minimumPushes(self, word: str) -> int:
        counts: list[int] = [0 for _ in range(26)]
        for char in word:
            counts[ord(char) - ord("a")] += 1
        counts.sort(reverse=True)

        res = 0
        for ind in range(26):
            if counts[ind] == 0:
                break
            res += counts[ind] * (ind // 8 + 1)

        return res
