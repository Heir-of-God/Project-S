from collections import defaultdict


class Solution:
    def singleNumber(self, nums: list[int]) -> list[int]:
        n: int = len(nums)
        result: list[int] = [0, 0]
        index = 0

        for i in range(n):
            found = False
            for j in range(n):
                if i != j and nums[i] == nums[j]:
                    found = True
                    break
            if not found:
                result[index] = nums[i]
                index += 1
                if index == 2:
                    break

        return result


class Solution:
    def singleNumber(self, nums: list[int]) -> list[int]:
        freq = defaultdict(int)  # number -> appear_number
        for n in nums:
            freq[n] += 1

        res: list[int] = []
        for num, f in freq.items():
            if f == 1:
                res.append(num)

        return res


class Solution:
    def singleNumber(self, nums: list[int]) -> list[int]:
        overall_xor = 0
        for n in nums:
            overall_xor ^= n
        first_group_xor = 0
        second_group_xor = 0

        bit_pos_dif = 0
        while (overall_xor >> bit_pos_dif) & 1 != 1:
            bit_pos_dif += 1

        for num in nums:
            if (num >> bit_pos_dif) & 1 == 1:
                first_group_xor ^= num
            else:
                second_group_xor ^= num

        return [first_group_xor, second_group_xor]
