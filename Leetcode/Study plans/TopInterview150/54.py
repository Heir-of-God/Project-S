class MinStack:

    def __init__(self) -> None:
        self.stack: list[tuple[int, int]] = (
            []
        )  # tuple[0] - element at this position and tuple[1] minimum element from bottom to this element

    def push(self, val: int) -> None:
        if self.stack:
            last_min: int = self.stack[-1][1]
            new_min: int = min(last_min, val)
        else:
            new_min = val
        self.stack.append((val, new_min))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
