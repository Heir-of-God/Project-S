class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res: list[str] = []
        cur_combination: list[str] = []
        needed_length: int = n * 2

        def recursion(opened_num, cur_opened, cur_length) -> None:
            nonlocal res, cur_combination
            if cur_length == needed_length:
                res.append("".join(cur_combination))
            if opened_num != n:
                cur_combination.append("(")
                recursion(opened_num + 1, cur_opened + 1, cur_length + 1)
                cur_combination.pop()
            if cur_opened != 0:
                cur_combination.append(")")
                recursion(opened_num, cur_opened - 1, cur_length + 1)
                cur_combination.pop()

        recursion(0, 0, 0)

        return res
