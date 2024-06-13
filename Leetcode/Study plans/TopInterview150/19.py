class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n: int = len(s)
        res: int = 0
        ind: int = n - 1
        while s[ind] == " ":
            ind -= 1

        while ind != -1 and s[ind] != " ":
            res += 1
            ind -= 1

        return res
