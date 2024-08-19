class Solution:
    def minSteps(self, n: int) -> int:
        def recursion(cur_steps, cur_copied, cur_length, last_copied):
            if cur_length > n:
                return float("inf")
            if cur_length == n:
                return cur_steps

            copy = float("inf")
            paste = float("inf")
            if not last_copied:
                copy = recursion(cur_steps + 1, cur_length, cur_length, True)

            if cur_copied != 0:
                paste = recursion(cur_steps + 1, cur_copied, cur_length + cur_copied, False)

            return min(copy, paste)

        return recursion(0, 0, 1, False)


class Solution:
    def minSteps(self, n: int) -> int:
        dp = [float("inf") for _ in range(n + 1)]
        dp[1] = 0

        for length in range(2, n + 1, 1):
            for prev_length in range(1, length // 2 + 1, 1):
                if (length - prev_length) % prev_length == 0:
                    dp[length] = min(dp[length], dp[prev_length] + (length - prev_length) // prev_length + 1)
                    # steps for get prev number + steps to get from that number to this + 1 for copy

        return dp[n]
