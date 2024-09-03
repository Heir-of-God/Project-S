class Solution:
    def getLucky(self, s: str, k: int) -> int:
        def get_sum_from_num(num) -> int:
            res = 0
            while num > 0:
                res += num % 10
                num //= 10
            return res

        res: int = 0
        for char in s:
            n: int = ord(char) - ord("a") + 1
            res += get_sum_from_num(n)

        for _ in range(k - 1):
            res = get_sum_from_num(res)

        return res
