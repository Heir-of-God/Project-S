class Solution:
    def findLengthOfShortestSubarray(self, arr: list[int]) -> int:
        right: int = len(arr) - 1
        while right > 0 and arr[right] >= arr[right - 1]:
            right -= 1

        res: int = right
        left: int = 0
        while left < right and (left == 0 or arr[left - 1] <= arr[left]):
            while right < len(arr) and arr[left] > arr[right]:
                right += 1
            res = min(res, right - left - 1)
            left += 1

        return res
