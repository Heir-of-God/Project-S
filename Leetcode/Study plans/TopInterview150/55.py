class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack: list[int] = []

        def perform_operation(op) -> int:
            second_operand = stack.pop()
            first_operand = stack.pop()
            if op == "+":
                return first_operand + second_operand
            elif op == "-":
                return first_operand - second_operand
            elif op == "*":
                return first_operand * second_operand
            elif op == "/":
                return int(first_operand / second_operand)

        for token in tokens:
            if token in "+-*/":
                stack.append(perform_operation(token))
            else:
                stack.append(int(token))

        return stack[0]
