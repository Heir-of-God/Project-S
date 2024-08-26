class Solution:
    def exclusiveTime(self, n: int, logs: list[str]) -> list[int]:
        stack: list[int] = []
        res: list[int] = [0 for _ in range(n)]
        last_time: int = 0
        last_type: str = ""

        for event in logs:
            func, kind, time = event.split(":")
            func = int(func)
            time = int(time)

            if kind == "start":
                if stack:
                    res[stack[-1]] += time - last_time - (last_type == "end")
                stack.append(func)
            elif kind == "end":
                last_func = stack.pop()
                res[last_func] += time - last_time + (last_type == "start")

            last_time = time
            last_type = kind

        return res
