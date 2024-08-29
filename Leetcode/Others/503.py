# O(nlogn)
class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        n: int = len(nums)
        res: list[int] = [-1 for _ in range(n)]
        wait: list[tuple[int, int]] = []

        for ind in range(2 * n):
            num: int = nums[ind % n]
            while wait and wait[0][0] < num:
                _, res_ind = heappop(wait)
                res[res_ind] = num

            if ind < n:
                heappush(wait, (num, ind))

        return res


# further improvement, O(n)
class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        n: int = len(nums)
        res: list[int] = [-1 for _ in range(n)]
        stack: list[int] = []

        for ind in range(2 * n):
            num: int = nums[ind % n]
            while stack and nums[stack[-1]] < num:
                res_ind: int = stack.pop()
                res[res_ind] = num

            if ind < n:
                stack.append(ind)

        return res
