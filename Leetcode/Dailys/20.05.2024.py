class Solution:
    def subsetXORSum(self, nums: list[int]) -> int:
        n = len(nums)

        def find_sum(cur_ind, cur_num):
            if cur_ind == n:  # if we reached the bound of the array then just return accumulated XORed number so far
                return cur_num

            include_in_xor = find_sum(cur_ind + 1, cur_num ^ nums[cur_ind])  # Sum if we include this elements
            not_include_in_xor = find_sum(cur_ind + 1, cur_num)  # Sum if we don't include this element

            return include_in_xor + not_include_in_xor  # Sum of both occasions

        return find_sum(0, 0)  # cur_num initially = 0 cause 0 ^ (any_number) = any_number


class Solution:
    def subsetXORSum(self, nums: list[int]) -> int:
        result = 0
        # Saving all "1" bits
        for num in nums:
            result |= num
        # Finding the sum (equivalent to (2^(x - 1)) * 2^(n - 1) )
        return result << (len(nums) - 1)
