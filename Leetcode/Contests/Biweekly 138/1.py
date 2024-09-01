class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        res = 0
        for ind in range(4):
            dig1, dig2, dig3 = num1 % 10, num2 % 10, num3 % 10
            num1 //= 10
            num2 //= 10
            num3 //= 10
            mn = min(dig1, dig2, dig3) * 10**ind
            res += mn

        return res
