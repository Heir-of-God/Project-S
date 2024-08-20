class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        def get_digit_sum(num) -> int:
            res = 0
            while num > 0:
                res += num % 10
                num //= 10

            return res

        cur_sum: int = get_digit_sum(n)
        cur_step: int = 0
        res: int = 0

        while cur_sum > target:
            cur_dig: int = n % 10 + (1 if cur_step else 0)
            to_make_zero_need_to_add: int = 10 - cur_dig
            cur_sum = cur_sum - cur_dig + 1
            res = to_make_zero_need_to_add * 10**cur_step + res
            n //= 10
            cur_step += 1

        return res
