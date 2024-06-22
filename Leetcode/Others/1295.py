class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        def get_number_of_digits(num) -> int:
            cur_mlt = 1
            while (num // (10**cur_mlt)) != 0:
                cur_mlt += 1
            return cur_mlt

        res: int = 0
        for num in nums:
            digits_num: int = get_number_of_digits(num)
            res += not digits_num & 1

        return res
