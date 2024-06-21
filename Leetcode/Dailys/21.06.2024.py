class Solution:
    def maxSatisfied(self, customers: list[int], grumpy: list[int], minutes: int) -> int:
        n: int = len(customers)
        res: int = 0
        cur_while_grumpy: int = 0
        mx_while_grumpy: int = 0
        left: int = 0

        for right in range(0, n, 1):
            if grumpy[right] == 0:
                res += customers[right]
            else:
                cur_while_grumpy += customers[right]

            while right - left + 1 > minutes:
                if grumpy[left] == 1:
                    cur_while_grumpy -= customers[left]
                left += 1

            mx_while_grumpy = max(cur_while_grumpy, mx_while_grumpy)

        return res + mx_while_grumpy
