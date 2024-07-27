class Solution:
    def minOperations(self, n: int) -> int:
        target: int = 2 * (n // 2) + (n & 1)
        sm: int = ((1 + (2 * (n // 2 - 1) + 1)) // 2) * (n // 2)

        return target * (n // 2) - sm
