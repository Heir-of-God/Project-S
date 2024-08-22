class Solution:
    def maxValueOfCoins(self, piles: list[list[int]], k: int) -> int:
        n: int = len(piles)
        piles_lengths: list[int] = [len(pile) for pile in piles]
        for pile_ind in range(n):
            for ind in range(1, piles_lengths[pile_ind], 1):
                piles[pile_ind][ind] += piles[pile_ind][ind - 1]

        memo: dict[tuple, int] = {}

        def recursion(cur_pile_ind, cur_k) -> int:
            if cur_pile_ind >= n or cur_k == 0:
                return 0
            if (cur_pile_ind, cur_k) in memo:
                return memo[(cur_pile_ind, cur_k)]

            # not take any coins
            local_res: int = recursion(cur_pile_ind + 1, cur_k)
            # take some
            for take_number in range(1, min(cur_k, piles_lengths[cur_pile_ind]) + 1, 1):
                local_res = max(
                    local_res, recursion(cur_pile_ind + 1, cur_k - take_number) + piles[cur_pile_ind][take_number - 1]
                )

            memo[(cur_pile_ind, cur_k)] = local_res
            return local_res

        res: int = recursion(0, k)
        return res
