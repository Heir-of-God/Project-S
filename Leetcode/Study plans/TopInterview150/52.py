class Solution:
    def isValid(self, s: str) -> bool:
        stack: list[str] = []
        matching: dict[str, str] = {"(": ")", "{": "}", "[": "]"}

        for char in s:
            if char in "([{":
                stack.append(char)
            else:
                if not stack or matching[stack.pop()] != char:
                    return False

        return not stack
