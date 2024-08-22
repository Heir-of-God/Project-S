class Solution:
    def findComplement(self, num: int) -> int:
        xor = 0
        n: int = num
        while n != 0:
            n >>= 1
            xor <<= 1
            xor += 1

        return num ^ xor
