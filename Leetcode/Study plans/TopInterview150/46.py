class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        closest_indeces: dict[int, int] = {}

        for ind, num in enumerate(nums):
            if num in closest_indeces:
                if ind - closest_indeces[num] <= k:
                    return True
            closest_indeces[num] = ind

        return False
