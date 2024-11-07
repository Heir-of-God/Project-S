class Solution:
    def largestCombination(self, candidates: list[int]) -> int:
        mx: int = max(candidates)
        num_of_nums_that_have_bit: list[int] = []

        while mx > 0:
            num_of_nums_that_have_bit.append(0)
            mx >>= 1

        def record_bits(num) -> None:
            i = 0
            while num > 0:
                num_of_nums_that_have_bit[i] += num & 1
                num >>= 1
                i += 1

        for num in candidates:
            record_bits(num)

        return max(num_of_nums_that_have_bit)
