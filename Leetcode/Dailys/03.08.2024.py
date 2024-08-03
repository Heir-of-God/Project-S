class Solution:
    def canBeEqual(self, target: list[int], arr: list[int]) -> bool:
        counting_target: list[int] = [0 for _ in range(1000)]
        counting_arr: list[int] = [0 for _ in range(1000)]

        for num in target:
            counting_target[num - 1] += 1

        for num in arr:
            counting_arr[num - 1] += 1

        return counting_target == counting_arr
