class Solution:
    def maxChunksToSorted(self, arr: list[int]) -> int:
        seen: set[int] = set()
        cur_need: int = 0
        res: int = 0

        for cur_num_pos, el in enumerate(arr):
            seen.add(el)
            if el == cur_need:
                while cur_need in seen:
                    cur_need += 1
            if cur_need > cur_num_pos:
                res += 1

        return res
