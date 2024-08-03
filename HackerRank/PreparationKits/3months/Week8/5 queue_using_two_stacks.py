class Queue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def add_element(self, x):
        self.stack1.append(x)

    def _refresh_queue(self):
        for _ in range(len(self.stack1)):
            self.stack2.append(self.stack1.pop())

    def pop_element(self):
        if not self.stack2:
            self._refresh_queue()
        return self.stack2.pop()

    def print_front(self):
        if not self.stack2:
            self._refresh_queue()
        print(self.stack2[-1])


q = int(input())
queue = Queue()

for _ in range(q):
    c: str = input()
    if c[0] == "1":
        c, val = c.split()
        queue.add_element(val)
    elif c[0] == "2":
        queue.pop_element()
    elif c[0] == "3":
        queue.print_front()
