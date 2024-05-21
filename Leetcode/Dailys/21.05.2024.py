class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res: list[list[int]] = [[]]

        for num in nums:
            res += [curr + [num] for curr in res]

        return res


class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res: list[list[int]] = []
        n: int = len(nums)

        def recursion(cur_index, curr) -> None:
            res.append(curr[:])

            for index_of_next in range(cur_index, n):
                curr.append(nums[index_of_next])
                recursion(index_of_next + 1, curr)
                curr.pop()

        recursion(0, [])

        return res
