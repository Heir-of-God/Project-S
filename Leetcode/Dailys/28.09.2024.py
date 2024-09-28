class MyCircularDeque:
    def __init__(self, k: int):
        self.v = [-1] * k
        self.front = 0
        self.back = 0
        self.cur_size = 0
        self.max_size = k

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        self.front = (self.front - 1 + self.max_size) % self.max_size
        self.v[self.front] = value
        self.cur_size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self.v[self.back] = value
        self.back = (self.back + 1) % self.max_size
        self.cur_size += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False

        self.v[self.front] = -1
        self.front = (self.front + 1) % self.max_size
        self.cur_size -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False

        if self.back == 0:
            self.back = self.max_size - 1
        else:
            self.back -= 1

        self.v[self.back] = -1
        self.cur_size -= 1
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.v[self.front]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        if self.back == 0:
            return self.v[self.max_size - 1]
        else:
            return self.v[self.back - 1]

    def isEmpty(self) -> bool:
        return self.cur_size == 0

    def isFull(self) -> bool:
        return self.cur_size == self.max_size
