class Solution:
    def maximumBobPoints(self, numArrows: int, aliceArrows: list[int]) -> list[int]:
        cur_state: list[int] = [0 for _ in range(12)]
        cur_res: list[int] = [0 for _ in range(12)]
        extra_arrows = 0
        cur_max = 0

        def recursion(cur_ind, cur_arrows, cur_points) -> None:
            nonlocal cur_max, cur_res, cur_state, extra_arrows

            if cur_ind == 12:
                if cur_points > cur_max:
                    extra_arrows = cur_arrows
                    cur_max = cur_points
                    cur_res = cur_state[:]
                return

            alice_shots = aliceArrows[cur_ind]
            # take this position
            if cur_arrows > alice_shots:
                cur_state[cur_ind] = alice_shots + 1
                recursion(cur_ind + 1, cur_arrows - alice_shots - 1, cur_points + cur_ind)
                cur_state[cur_ind] = 0
            # don't take
            recursion(cur_ind + 1, cur_arrows, cur_points)

        recursion(0, numArrows, 0)
        cur_res[0] += extra_arrows
        return cur_res
