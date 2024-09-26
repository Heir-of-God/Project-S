class MyCalendar:
    def __init__(self) -> None:
        self.events: list[list[int]] = []  # self.events[i] = [start_time, end_time]

    def book(self, start: int, end: int) -> bool:
        left: int = 0
        right: int = len(self.events) - 1
        res = -1  # prev event index

        while left <= right:
            mid: int = (left + right) // 2

            if self.events[mid][0] <= start:
                res: int = mid
                left = mid + 1
            else:
                right = mid - 1

        if res == -1:
            res = -1 if left == 0 else len(self.events) - 1

        if res != -1 and (self.events and self.events[res][1] > start):
            return False

        if res != len(self.events) - 1 and (self.events and self.events[res + 1][0] < end):
            return False

        self.events.insert(res + 1, [start, end])
        return True
