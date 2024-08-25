from collections import defaultdict


class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        counts: list[defaultdict[int, int]] = [defaultdict(int), defaultdict(int)]
        for ind, el in enumerate(nums):
            counts[ind & 1][el] += 1

        def get_two_mins(count_ind) -> list[list[int]]:
            res: list[list[int]] = [[0, 0], [0, 0]]
            for el, count in counts[count_ind].items():
                if count >= res[0][1]:
                    res[1] = res[0][:]
                    res[0][1] = count
                    res[0][0] = el
                elif count >= res[1][1]:
                    res[1][1] = count
                    res[1][0] = el

            return res

        topcount_even_elem: list[list[int]] = get_two_mins(0)
        topcount_odd_elem: list[list[int]] = get_two_mins(1)

        n: int = len(nums)
        even_positions: int = n // 2
        odd_positions: int = n - even_positions

        if topcount_even_elem[0][0] != topcount_odd_elem[0][0]:
            return (even_positions - topcount_even_elem[0][1]) + (odd_positions - topcount_odd_elem[0][1])

        return min(
            (even_positions - topcount_even_elem[1][1]) + (odd_positions - topcount_odd_elem[0][1]),
            (even_positions - topcount_even_elem[0][1]) + (odd_positions - topcount_odd_elem[1][1]),
        )
