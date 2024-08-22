class Solution:
    def getStrongest(self, arr: list[int], k: int) -> list[int]:
        n: int = len(arr)
        arr.sort()
        median: int = arr[(n - 1) // 2]
        res: list[int] = []
        left: int = 0
        right: int = n - 1

        for _ in range(k):
            left_val: int = median - arr[left]
            right_val: int = arr[right] - median

            if right_val >= left_val:
                res.append(arr[right])
                right -= 1
            else:
                res.append(arr[left])
                left += 1

        return res
