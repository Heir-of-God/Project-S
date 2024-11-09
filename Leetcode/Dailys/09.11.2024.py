class Solution:
    def minEnd(self, n: int, x: int) -> int:
        result: int = x
        n -= 1
        mask: int = 1

        while n > 0:
            if (mask & x) == 0:
                result |= (n & 1) * mask
                n >>= 1
            mask <<= 1

        return result
