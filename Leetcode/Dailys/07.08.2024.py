ones: list[str] = [
    "",
    "One",
    "Two",
    "Three",
    "Four",
    "Five",
    "Six",
    "Seven",
    "Eight",
    "Nine",
    "Ten",
    "Eleven",
    "Twelve",
    "Thirteen",
    "Fourteen",
    "Fifteen",
    "Sixteen",
    "Seventeen",
    "Eighteen",
    "Nineteen",
]
tens: list[str] = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
thsnds: list[str] = ["", "Thousand", "Million", "Billion"]


class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        def form_name_for_number(number: int, res: list[str]) -> None:
            if number < 20:
                if number != 0:
                    res.append(ones[number])
            elif number < 100:
                res.append(tens[number // 10])
                if number % 10 != 0:
                    res.append(ones[number % 10])
            elif number < 1000:
                if number // 100 != 0:
                    res.append(ones[number // 100] + " Hundred")
                form_name_for_number(number % 100, res)
            else:
                for group_ind_from_end in range(3, -1, -1):
                    if number >= 10 ** (3 * group_ind_from_end):
                        group_num = (number // (10 ** (3 * group_ind_from_end))) % 1000
                        if group_num != 0:
                            form_name_for_number(group_num, res)
                            if group_ind_from_end != 0:
                                res.append(thsnds[group_ind_from_end])

        res: list[str] = []
        form_name_for_number(num, res)
        return " ".join(res)
