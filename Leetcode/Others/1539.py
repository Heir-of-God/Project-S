class Solution:
    def findKthPositive(self, arr: list[int], k: int) -> int:
        arr = [0] + arr + [2500]
        n: int = len(arr)

        for ind in range(1, n, 1):
            missing: int = arr[ind] - arr[ind - 1] - 1
            if missing >= k:
                return arr[ind - 1] + k
            k -= missing

        return -1
