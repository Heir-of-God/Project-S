class Solution:
    def stoneGameII(self, piles: list[int]) -> int:
        n: int = len(piles)

        memo: dict[tuple[int, int, bool], int] = {}

        def recursion(cur_ind, M, alice_turn) -> int:
            if cur_ind >= n:
                return 0
            if (cur_ind, M, alice_turn) in memo:
                return memo[(cur_ind, M, alice_turn)]

            res: int = 0 if alice_turn else float("inf")
            total_add = 0
            for takes_stones in range(1, 2 * M + 1, 1):
                if cur_ind + takes_stones - 1 >= n:
                    break
                total_add += piles[cur_ind + takes_stones - 1]
                if alice_turn:
                    res = max(res, recursion(cur_ind + takes_stones, max(M, takes_stones), False) + total_add)
                else:
                    res = min(res, recursion(cur_ind + takes_stones, max(M, takes_stones), True))

            memo[(cur_ind, M, alice_turn)] = res
            return res

        res: int = recursion(0, 1, True)
        return res


class Solution:
    def stoneGameII(self, piles: list[int]) -> int:
        n: int = len(piles)
        suffix_sum: list[int] = [0 for _ in range(n)]
        suffix_sum[n - 1] = piles[n - 1]
        for ind in range(n - 2, -1, -1):
            suffix_sum[ind] = suffix_sum[ind + 1] + piles[ind]
        dp: list[list[int]] = [[0 for _ in range(n + 1)] for _ in range(n)]  # dp[ind][M]

        for ind in range(n - 1, -1, -1):
            for possible_M in range(1, n + 1, 1):
                if ind + possible_M * 2 >= n:  # alice can take all stones
                    dp[ind][possible_M] = suffix_sum[ind]
                else:
                    for take_stones in range(1, 2 * possible_M + 1):
                        dp[ind][possible_M] = max(
                            dp[ind][possible_M], suffix_sum[ind] - dp[ind + take_stones][max(possible_M, take_stones)]
                        )

        return dp[0][1]
