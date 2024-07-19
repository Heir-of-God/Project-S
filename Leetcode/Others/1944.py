class Solution:
    def canSeePersonsCount(self, heights: list[int]) -> list[int]:
        stack: list[int] = []
        n: int = len(heights)
        res: list[int] = [0 for _ in range(n)]

        for ind in range(n - 1, -1, -1):
            cur_h: int = heights[ind]

            while stack and stack[-1] <= cur_h:
                res[ind] += 1
                stack.pop()
            if stack:
                res[ind] += 1

            stack.append(cur_h)

        return res
