class Solution:
    def numberOfAlternatingGroups(self, colors: list[int], k: int) -> int:
        res: int = 0
        cur_length: int = 0
        last: int = -1

        for char in colors + colors[: k - 1]:
            if char == last:
                cur_length = 1
            else:
                cur_length += 1
                last = char
                if cur_length == k:
                    res += 1
                    cur_length -= 1

        return res
