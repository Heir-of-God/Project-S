class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        res = 0

        while a != 0 or b != 0 or c != 0:
            bit_a: int = a & 1
            bit_b: int = b & 1
            bit_c: int = c & 1

            a >>= 1
            b >>= 1
            c >>= 1

            if bit_c == 1 and 1 not in (bit_a, bit_b):
                res += 1
            elif bit_c == 0:
                res += bit_a
                res += bit_b

        return res
