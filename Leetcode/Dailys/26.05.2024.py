class Solution:
    def checkRecord(self, n: int) -> int:
        temp: list[list[list[int]]] = [
            [[-1 for _ in range(3)] for _ in range(2)] for _ in range(n)
        ]  # temp[cur_ind][count_a][count_l]
        MOD: int = 10**9 + 7

        def check_all_records(cur_ind, count_a, count_l) -> int:
            if cur_ind == n:
                return 1
            if temp[cur_ind][count_a][count_l] != -1:
                return temp[cur_ind][count_a][count_l]
            with_a_next: int = check_all_records(cur_ind + 1, count_a + 1, 0) if count_a == 0 else 0
            with_l_next: int = 0 if count_l == 2 else check_all_records(cur_ind + 1, count_a, count_l + 1)
            with_p_next: int = check_all_records(cur_ind + 1, count_a, 0)
            total: int = (with_a_next + with_l_next + with_p_next) % MOD

            temp[cur_ind][count_a][count_l] = total
            return total

        return check_all_records(0, 0, 0)


class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = 1000000007

        dp_last: list[list[int]] = [[0 for _ in range(3)] for _ in range(2)]  # previous state
        dp_current: list[list[int]] = [[0 for _ in range(3)] for _ in range(2)]  # current state

        dp_last[0][0] = 1  # empty string

        for _ in range(n):
            for count_a in range(2):
                for count_l in range(3):
                    # choose "P"
                    dp_current[count_a][0] = (dp_current[count_a][0] + dp_last[count_a][count_l]) % MOD
                    # choose "A"
                    if count_a == 0:
                        dp_current[count_a + 1][0] = (dp_current[count_a + 1][0] + dp_last[count_a][count_l]) % MOD
                    # Choose "L"
                    if count_l < 2:
                        dp_current[count_a][count_l + 1] = (
                            dp_current[count_a][count_l + 1] + dp_last[count_a][count_l]
                        ) % MOD

            dp_last = dp_current  # Reference current to previous
            dp_current = [[0 for _ in range(3)] for _ in range(2)]  # make new current

        # Sum up the counts for all combinations of length 'n' with different count_a and count_l.
        res: int = sum(dp_last[count_a][count_l] for count_a in range(2) for count_l in range(3)) % MOD
        return res
