class Solution:
    def maxDistance(self, arrays: list[list[int]]) -> int:
        max1: list[int] = [0, -float("inf")]  # ind, val
        max2: list[int] = [0, -float("inf")]  # ind, val
        min1: list[int] = [0, float("inf")]  # ind, val
        min2: list[int] = [0, float("inf")]  # ind, val

        for ind, arr in enumerate(arrays):
            mx: int = arr[-1]
            mn: int = arr[0]

            if mx > max1[1] or (mx == max1 and max1[0] == min1[0]):
                max2, max1 = max1, [ind, mx]
            elif mx > max2[1]:
                max2 = [ind, mx]

            if mn < min1[1] or (mn == min1 and max1[0] == min1[0]):
                min2, min1 = min1, [ind, mn]
            elif mn < min2[1]:
                min2 = [ind, mn]

        if max1[0] != min1[0]:
            return max1[1] - min1[1]
        return max(max1[1] - min2[1], max2[1] - min1[1])
