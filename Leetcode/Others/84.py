class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        n: int = len(heights)
        res: int = 0
        stack: list[tuple[int, int]] = []

        for ind, height in enumerate(heights):
            new_ind: int = ind
            while stack and stack[-1][1] > height:
                start_ind, that_height = stack.pop()
                new_ind = start_ind
                res = max(res, that_height * (ind - start_ind))
            stack.append((new_ind, height))

        for start_ind, height in stack:
            res = max(res, height * (n - start_ind))

        return res
