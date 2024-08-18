class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        n: int = len(s)
        res = list(s)

        left = 0
        right: int = n - 1

        while left < right:
            while left < right and not s[left].isalpha():
                left += 1
            while left < right and not s[right].isalpha():
                right -= 1
            res[left], res[right] = res[right], res[left]
            left += 1
            right -= 1

        return "".join(res)


class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        n: int = len(s)
        res = list(s)
        letters: list[str] = []

        for char in res:
            if char.isalpha():
                letters.append(char)
        letters.reverse()
        cur_ind_change = 0
        for ind in range(n):
            if s[ind].isalpha():
                res[ind] = letters[cur_ind_change]
                cur_ind_change += 1

        return "".join(res)
