class Solution:
    def countConsistentStrings(self, allowed: str, words: list[str]) -> int:
        allowed = set(allowed)
        res = 0

        for word in words:
            flag = True
            for char in word:
                if char not in allowed:
                    flag = False
                    break
            res += flag

        return res
