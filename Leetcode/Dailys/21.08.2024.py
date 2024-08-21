class Solution:
    def strangePrinter(self, s: str) -> int:
        def recursion(start_ind, end_ind) -> int:
            if start_ind > end_ind:
                return 0
            if memo[start_ind][end_ind] != -1:
                return memo[start_ind][end_ind]

            # print first character only
            local_min: int = 1 + recursion(start_ind + 1, end_ind)

            # print up to some matching character
            for range_end in range(start_ind + 1, end_ind + 1, 1):
                if s[start_ind] == s[range_end]:
                    local_min = min(local_min, recursion(start_ind, range_end - 1) + recursion(range_end + 1, end_ind))
                    # Why first addition is either recursion(start_ind, range_end - 1) or recursion(start_ind + 1, range_end) (both works)?
                    # We can imagine that we already printed one of the matching characters, we don't add here any operation because it will
                    # be added inside this recursion call (we still need to somehow print the second matching character)

            memo[start_ind][end_ind] = local_min
            return local_min

        new: list[str] = []
        prev = "_"

        for char in s:
            if char != prev:
                new.append(char)
            prev = char

        s = "".join(new)
        n: int = len(s)
        memo: list[list[int]] = [[-1 for _ in range(n)] for _ in range(n)]
        res: int = recursion(0, n - 1)

        return res


class Solution:
    def strangePrinter(self, s: str) -> int:
        new = []
        prev = "_"

        for char in s:
            if char != prev:
                new.append(char)
            prev = char

        s = "".join(new)
        n: int = len(s)
        dp: list[list[int]] = [[-1 for _ in range(n)] for _ in range(n)]
        for ind in range(n):
            dp[ind][ind] = 1  # to print one single character you need 1 move

        for length in range(2, n + 1, 1):
            for start_ind in range(0, n - length + 1, 1):
                end_ind = start_ind + length - 1
                dp[start_ind][end_ind] = 1 + dp[start_ind + 1][end_ind]
                for matching_ind in range(start_ind + 1, end_ind + 1, 1):
                    if s[start_ind] == s[matching_ind]:
                        dp[start_ind][end_ind] = min(
                            dp[start_ind][end_ind],
                            dp[start_ind][matching_ind - 1]
                            + (dp[matching_ind + 1][end_ind] if matching_ind + 1 <= end_ind else 0),
                        )

        return dp[0][n - 1]
