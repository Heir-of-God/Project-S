class Solution:
    def calculate(self, s: str) -> int:
        cur_number: int = 0
        last_sign: int = 1
        stack: list[int] = []
        res = 0

        for i in range(len(s)):  # iterate till last character
            char: str = s[i]
            if char.isdigit():  # process if there is digit
                cur_number = cur_number * 10 + int(char)

            elif char in "-+":  # check for - and +
                res += cur_number * last_sign
                last_sign = -1 if char == "-" else 1
                cur_number = 0

            elif char == "(":
                stack.append(res)
                stack.append(last_sign)
                res = 0
                last_sign = 1

            elif char == ")":
                res += last_sign * cur_number
                res *= stack.pop()
                res += stack.pop()
                cur_number = 0

        return res + cur_number * last_sign
