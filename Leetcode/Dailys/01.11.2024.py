class Solution:
    def makeFancyString(self, s: str) -> str:
        stack: list[str] = []

        for char in s:
            if len(stack) < 2 or (stack[-1], stack[-2]) != (char, char):
                stack.append(char)

        return "".join(stack)
