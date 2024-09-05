class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n1: int = len(word1)
        n2: int = len(word2)
        ind: int = 0
        res: str = ""

        for ind in range(min(n1, n2)):
            res += word1[ind] + word2[ind]

        return res + word1[ind + 1 :] if ind == n2 - 1 else res + word2[ind + 1 :]
