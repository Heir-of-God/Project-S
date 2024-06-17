class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for first_num in range(0, int(c**0.5 + 1), 1):
            second_num: float = (c - first_num**2) ** 0.5
            if second_num == int(second_num):
                return True
        return False


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        first_num = 0
        second_num = int(c**0.5)
        while first_num <= second_num:
            curr_sum: int = first_num * first_num + second_num * second_num
            if curr_sum == c:
                return True
            elif curr_sum < c:
                first_num += 1
            else:
                second_num -= 1

        return False
