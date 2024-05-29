class Solution:
    def numSteps(self, s: str) -> int:
        operations = 0
        carry = 0
        for ind in range(len(s) - 1, 0, -1):
            digit: int = int(s[ind]) + carry
            if digit % 2 == 1:
                operations += 2
                carry = 1
            else:
                operations += 1

        return operations + carry
