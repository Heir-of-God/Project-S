class Solution:
    def smallestDistancePair(self, nums: list[int], k: int) -> int:
        def more_than_k_pairs(diff: int) -> bool:
            count: int = 0
            left: int = 0
            right: int = 0

            while right != n - 1:
                right += 1
                while left != right and nums[right] - nums[left] > diff:
                    left += 1
                count += right - left
                if count >= k:
                    return True
            return False

        n: int = len(nums)
        left: int = 0
        nums.sort()
        right: int = nums[-1]

        while right != left:
            mid: int = (right + left) // 2
            search_left_part: bool = more_than_k_pairs(mid)

            if search_left_part:
                right = mid
            else:
                left = mid + 1

        return right
