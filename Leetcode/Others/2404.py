class Solution:
    def mostFrequentEven(self, nums: list[int]) -> int:
        even_counter: dict[int, int] = {}
        for n in nums:
            if n & 1 == 0:
                if n not in even_counter:
                    even_counter[n] = 0
                even_counter[n] += 1

        res: int = -1
        c: int = 0
        for val, count in even_counter.items():
            if count > c or (val < res and c == count):
                res = val
                c = count

        return res
