class Solution:
    def minOperations(self, logs: list[str]) -> int:
        res: int = 0

        for log in logs:
            if log == "../":
                res -= 1 if res > 0 else 0
            elif log != "./":
                res += 1

        return res


class Solution:
    def minOperations(self, logs: list[str]) -> int:
        paths_stack: list[str] = []

        for log in logs:
            if log == "../":
                if paths_stack:
                    paths_stack.pop()
            elif log != "./":
                paths_stack.append(log)

        return len(paths_stack)
