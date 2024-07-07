class Solution:
    def isHappy(self, n: int) -> bool:

        def get_square_sum(num):
            res = 0
            while num > 0:
                dig = num % 10
                num //= 10
                res += dig**2

            return res

        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = get_square_sum(n)

        return n == 1


class Solution:
    def isHappy(self, n: int) -> bool:

        def get_square_sum(num):
            res = 0
            while num > 0:
                dig = num % 10
                num //= 10
                res += dig**2

            return res

        while n != 1 and n != 4:
            n = get_square_sum(n)

        return n == 1
