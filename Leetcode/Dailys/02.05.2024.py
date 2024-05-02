# class Solution:
#     def findMaxK(self, nums: list[int]) -> int:
#         res = -1
#         negs = set()
#         for n in nums:
#             if n < 0:
#                 negs.add(n)

#         for n in nums:
#             if n > 0:
#                 if -n in negs:
#                     if n > res:
#                         res = n

#         return res
# O(n) time but O(n) memory


class Solution:
    def findMaxK(self, nums: list[int]) -> int:
        nums.sort()
        l, r = 0, len(nums) - 1

        while l < r and nums[l] < 0 and nums[r] > 0:
            if nums[r] + nums[l] == 0:
                return nums[r]
            elif nums[l] < -nums[r]:
                l += 1
            else:
                r -= 1

        return -1


# O(n*logn) time (for sorting) but O(1) memory
