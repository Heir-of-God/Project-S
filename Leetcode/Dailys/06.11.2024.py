class Solution:
    def canSortArray(self, nums: list[int]) -> bool:
        bits_nums: dict[int, int] = {}

        def get_bits(num) -> int:
            if num in bits_nums:
                return bits_nums[num]

            res = 0

            while num > 0:
                res += num & 1
                num >>= 1

            bits_nums[num] = res
            return res

        while True:
            swap_perfomed = False

            for ind in range(1, len(nums), 1):
                if nums[ind - 1] > nums[ind]:
                    bits1: int = get_bits(nums[ind - 1])
                    bits2: int = get_bits(nums[ind])

                    if bits1 != bits2:
                        return False
                    nums[ind - 1], nums[ind] = nums[ind], nums[ind - 1]
                    swap_perfomed = True

            if not swap_perfomed:
                break

        return True


class Solution:
    def canSortArray(self, nums: list[int]) -> bool:
        bits_nums: dict[int, int] = {}

        def get_bits(num) -> int:
            if num in bits_nums:
                return bits_nums[num]

            res = 0

            while num > 0:
                res += num & 1
                num >>= 1

            bits_nums[num] = res
            return res

        num_of_segment_bits: int = get_bits(nums[0])
        max_of_segment: int = nums[0]
        min_of_segment: int = nums[0]

        max_of_prev_segment: int = float("-inf")
        for i in range(1, len(nums)):
            if get_bits(nums[i]) == num_of_segment_bits:
                max_of_segment = max(max_of_segment, nums[i])
                min_of_segment = min(min_of_segment, nums[i])
            else:
                if min_of_segment < max_of_prev_segment:
                    return False
                max_of_prev_segment = max_of_segment
                max_of_segment = nums[i]
                min_of_segment = nums[i]
                num_of_segment_bits = get_bits(nums[i])

        if min_of_segment < max_of_prev_segment:
            return False

        return True
