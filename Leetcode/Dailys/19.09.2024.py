class Solution:
    def diffWaysToCompute(self, expression: str) -> list[int]:
        operations: dict[str, callable[int, int]] = {
            "+": lambda x, y: x + y,
            "*": lambda x, y: x * y,
            "-": lambda x, y: x - y,
        }

        def recursion(left, right) -> list[int]:
            if right - left in (1, 2):
                return [int(expression[left:right])]

            res: list[int] = []
            for ind in range(left, right):
                char: str = expression[ind]
                if char in operations:
                    left_part: list[int] = recursion(left, ind)
                    right_part: list[int] = recursion(ind + 1, right)

                    for num1 in left_part:
                        for num2 in right_part:
                            res.append(operations[char](num1, num2))
            return res

        return recursion(0, len(expression))
