class Solution:
    def minIncrementForUnique(self, nums: list[int]) -> int:
        n: int = len(nums)
        res: int = 0
        nums.sort()
        for cur_ind in range(1, n):
            cur_num: int = nums[cur_ind]
            if cur_num <= nums[cur_ind - 1]:
                steps: int = nums[cur_ind - 1] - cur_num + 1
                nums[cur_ind] = steps + cur_num
                res += steps

        return res


class Solution:
    def minIncrementForUnique(self, nums: list[int]) -> int:
        n: int = len(nums)
        max_val: int = max(nums)
        res: int = 0
        count: list[int] = [0] * (
            n + max_val + 1
        )  # if every element in nums is max we will need extra space to make n - 1 elements bigger

        for val in nums:
            count[val] += 1

        for cur_ind in range(len(count)):
            if count[cur_ind] not in (0, 1):
                steps: int = count[cur_ind] - 1
                count[cur_ind + 1] += steps
                count[cur_ind] = 1
                res += steps

        return res
