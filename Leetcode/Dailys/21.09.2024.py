class Solution:
    def lexicalOrder(self, n: int) -> list[int]:
        res: list[int] = []

        def dfs(cur_num) -> None:
            cur_num *= 10
            if cur_num > n:
                return

            for digit in range((1 if cur_num == 0 else 0), 10, 1):
                cur_num += digit
                if cur_num <= n:
                    res.append(cur_num)
                    dfs(cur_num)
                cur_num -= digit

            return

        dfs(0)
        return res
