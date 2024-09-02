class Solution:
    def chalkReplacer(self, chalk: list[int], k: int) -> int:
        sm: int = sum(chalk)
        k %= sm
        for ind, num in enumerate(chalk):
            if num > k:
                return ind
            k -= num

        return -1


class Solution:
    def chalkReplacer(self, chalk: list[int], k: int) -> int:
        n: int = len(chalk)
        for ind in range(1, n, 1):
            chalk[ind] += chalk[ind - 1]
        k %= chalk[-1]
        left: int = 0
        right: int = n - 1
        res: int = -1

        while left <= right:
            mid: int = (left + right) // 2
            mid_el: int = chalk[mid]

            if mid_el <= k:
                left = mid + 1
            else:
                res = mid
                right = mid - 1

        return res
