from typing import Counter


class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> list[str]:
        res: list[str] = []
        s1 = Counter(s1.split())
        s2 = Counter(s2.split())

        for word in s1:
            if s1[word] == 1 and word not in s2:
                res.append(word)

        for word in s2:
            if s2[word] == 1 and word not in s1:
                res.append(word)

        return res
