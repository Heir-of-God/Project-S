class Solution:
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        n: int = len(nums)
        left: int = 0
        left_first_odd_ind: int = left
        while left_first_odd_ind != n and nums[left_first_odd_ind] & 1 == 0:
            left_first_odd_ind += 1
        res: int = 0
        cur_count: int = 0

        for right in range(n):
            is_odd_here: bool = nums[right] & 1 == 1
            cur_count += is_odd_here
            if cur_count > k:
                cur_count -= 1
                left = left_first_odd_ind + 1
                left_first_odd_ind = left
                while left_first_odd_ind != n and nums[left_first_odd_ind] & 1 == 0:
                    left_first_odd_ind += 1
            if cur_count == k:
                res += left_first_odd_ind - left + 1

        return res
