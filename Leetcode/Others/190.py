class Solution:
    def reverseBits(self, n: int) -> int:
        res: int = 0
        for degree in range(31, -1, -1):
            if n == 0:
                break
            bit: int = n & 1
            n >>= 1
            if bit:
                res += 2**degree

        return res
