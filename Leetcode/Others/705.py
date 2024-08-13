class MyHashSet:

    def __init__(self) -> None:
        self.storing: list[bool] = [False for _ in range(10**6 + 1)]

    def add(self, key: int) -> None:
        self.storing[key] = True

    def remove(self, key: int) -> None:
        self.storing[key] = False

    def contains(self, key: int) -> bool:
        return self.storing[key]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
