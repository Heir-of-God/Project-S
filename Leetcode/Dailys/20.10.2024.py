class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stack = []

        for char in expression:
            if char in "&|!ft":
                stack.append(char)
            elif char == ")":
                if stack[-2] == "!":
                    val = stack.pop()
                    stack.pop()
                    stack.append("f" if val == "t" else "t")
                    continue

                val_or = False
                val_and = True

                while (operation := stack.pop()) not in "&|":
                    val_or = val_or or operation == "t"
                    val_and = val_and and operation == "t"

                if operation == "|":
                    stack.append("f" if not val_or else "t")
                else:
                    stack.append("f" if not val_and else "t")

        return True if stack[-1] == "t" else False
