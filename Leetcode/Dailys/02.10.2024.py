class Solution:
    def arrayRankTransform(self, arr: list[int]) -> list[int]:
        arr = [(el, i) for i, el in enumerate(arr)]
        arr.sort()
        res: list[int] = [0 for _ in range(len(arr))]
        cur_rank = 1

        for i, (_, ind) in enumerate(arr):
            if i != 0 and arr[i - 1][0] != arr[i][0]:
                cur_rank += 1
            res[ind] = cur_rank

        return res
