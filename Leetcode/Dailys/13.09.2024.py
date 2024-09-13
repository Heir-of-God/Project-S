class Solution:
    def xorQueries(self, arr: list[int], queries: list[list[int]]) -> list[int]:
        for i in range(1, len(arr)):
            arr[i] ^= arr[i - 1]

        res = []
        for left, right in queries:
            res.append(arr[right] ^ (arr[left - 1] if left != 0 else 0))

        return res
