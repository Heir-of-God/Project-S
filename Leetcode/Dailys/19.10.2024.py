class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        if n == 1:
            return "0"

        length = 2**n - 1
        mid_ind = (length - 1) // 2
        print(n, k, length, mid_ind)

        if (k - 1) == mid_ind:
            return "1"
        elif (k - 1) < mid_ind:
            return self.findKthBit(n - 1, k)
        else:
            print(length, k)
            return "1" if self.findKthBit(n - 1, length - k + 1) == "0" else "0"
