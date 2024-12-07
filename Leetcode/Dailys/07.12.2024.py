class Solution:
    def minimumSize(self, nums: list[int], maxOperations: int) -> int:
        def check(num) -> bool:
            res = 0
            for bag in nums:
                res += (bag - 1) // num
                if res > maxOperations:
                    return False
            return True

        left: int = 1
        right: int = max(nums)

        while left < right:
            mid: int = left + (right - left) // 2

            if check(mid):
                right = mid
            else:
                left = mid + 1

        return left
