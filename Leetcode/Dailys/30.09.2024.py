class CustomStack:

    def __init__(self, maxSize: int) -> None:
        self.stack: list[int] = [-1 for _ in range(maxSize)]
        self.inc: list[int] = [0 for _ in range(maxSize)]
        self.top: int = -1

    def push(self, x: int) -> None:
        if self.top != len(self.stack) - 1:
            self.top += 1
            self.stack[self.top] = x

    def pop(self) -> int:
        if self.top == -1:
            return self.top

        res: int = self.stack[self.top] + self.inc[self.top]
        if self.top > 0:
            self.inc[self.top - 1] += self.inc[self.top]
        self.inc[self.top] = 0
        self.top -= 1

        return res

    def increment(self, k: int, val: int) -> None:
        if self.top != -1:
            self.inc[min(self.top, k - 1)] += val
