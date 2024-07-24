class Solution:
    def sortJumbled(self, mapping: list[int], nums: list[int]) -> list[int]:
        def translate_integer(num: int) -> int:
            digits: list[str] = list(str(num))
            for i in range(len(digits)):
                digits[i] = str(mapping[int(digits[i])])
            return int("".join(digits))

        number_mapping: dict[int, int] = {}
        for num in nums:
            if num not in number_mapping:
                number_mapping[num] = translate_integer(num)
        nums.sort(key=lambda val: number_mapping[val])

        return nums


class Solution:
    def sortJumbled(self, mapping: list[int], nums: list[int]) -> list[int]:
        def translate_integer(num: int) -> int:
            if num == 0:  # edge case, we don't want return 0 but mapping value
                return mapping[0]
            res: int = 0
            cur_mult: int = 1  # to construct number we need every time multiple new digit
            while num > 0:
                digit = num % 10
                num //= 10
                res = mapping[digit] * cur_mult + res
                cur_mult *= 10

            return res

        number_mapping: dict[int, int] = {}
        for num in nums:
            if num not in number_mapping:
                number_mapping[num] = translate_integer(num)
        nums.sort(key=lambda val: number_mapping[val])

        return nums
