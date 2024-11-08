class Solution:
    def getMaximumXor(self, nums: list[int], maximumBit: int) -> list[int]:
        first_bits_setted: int = (1 << maximumBit) - 1

        # for _ in range(maximumBit):
        #     first_bits_setted <<= 1
        #     first_bits_setted += 1

        res: list[int] = []
        running_xor: int = 0
        for num in nums:
            num_first_bits: int = num & first_bits_setted
            running_xor ^= num_first_bits
            res.append(running_xor ^ first_bits_setted)

        return res[::-1]
