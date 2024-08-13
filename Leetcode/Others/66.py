class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        n: int = len(digits)
        add: bool = True
        cur_ind: int = n - 1

        while cur_ind >= 0 and add:
            cur: int = digits[cur_ind]
            digits[cur_ind] = (cur + 1) % 10
            add = (cur + 1) // 10
            cur_ind -= 1

        if add:
            digits = [1] + digits

        return digits
