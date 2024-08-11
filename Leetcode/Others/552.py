class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = 10**9 + 7
        prev_state: list[list[int]] = [[0, 0] for _ in range(3)]
        prev_state[0][0] = 1

        for _ in range(n):
            cur_state: list[list[int]] = [[0, 0] for _ in range(3)]
            # adding A to the end of every string
            cur_state[0][1] += sum([prev_state[i][0] for i in range(3)])
            # adding P to the end of every string
            cur_state[0][0] += sum([prev_state[i][0] for i in range(3)])
            cur_state[0][1] += sum([prev_state[i][1] for i in range(3)])
            # adding L to the end of every string
            for cur_late_days in range(1, 3):
                cur_state[cur_late_days][0] += prev_state[cur_late_days - 1][0]
                cur_state[cur_late_days][1] += prev_state[cur_late_days - 1][1]
            prev_state = [[i % MOD for i in row] for row in cur_state]

        return sum([sum(row) for row in prev_state]) % MOD
