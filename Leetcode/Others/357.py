# pure combinatorics
class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        def get_fact(num) -> int:
            res = 1
            for n in range(2, num + 1):
                res *= n
            return res

        res = 1
        facts: list[int] = [get_fact(i) for i in range(0, 10, 1)]

        for number_of_digits in range(1, n + 1):
            create_number_ways: int = 9 * (facts[9] // facts[9 - number_of_digits + 1])
            res += create_number_ways
        return res


# dynamic programming O(1)
class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        res: int = 1
        prev_dp: int = 1
        cur_add_to_end: int = 9  # how many digits you can add to end of every number

        for num_of_digits in range(1, n + 1, 1):
            prev_dp = prev_dp * cur_add_to_end
            res += prev_dp
            if num_of_digits >= 2:
                cur_add_to_end -= 1

        return res
