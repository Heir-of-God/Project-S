class Solution:
    def maxSumAfterPartitioning(self, arr: list[int], k: int) -> int:
        n: int = len(arr)
        dp: list[int] = [0 for _ in range(n + 1)]

        for number_of_elems in range(1, n + 1):
            max_elem = 0

            for last_included_ind in range(number_of_elems - 1, max(-1, number_of_elems - k - 1), -1):
                max_elem: int = max(max_elem, arr[last_included_ind])
                dp[number_of_elems] = max(
                    dp[number_of_elems], dp[last_included_ind] + max_elem * (number_of_elems - last_included_ind)
                )

        return dp[n]
