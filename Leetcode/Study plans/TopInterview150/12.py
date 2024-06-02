from random import randint


class RandomizedSet:

    def __init__(self) -> None:
        self.indexes: dict[int, int] = {}
        self.elems: list[int] = []
        self.n = 0

    def insert(self, val: int) -> bool:
        if val in self.indexes:
            return False
        self.n += 1
        self.elems.append(val)
        self.indexes[val] = self.n - 1
        return True

    def remove(self, val: int) -> bool:
        if not val in self.indexes:
            return False

        self.n -= 1
        el_ind: int = self.indexes[val]
        new_val: int = self.elems[-1]
        self.elems[el_ind] = new_val
        self.indexes[new_val] = el_ind
        self.elems.pop()
        del self.indexes[val]

        return True

    def getRandom(self) -> int:
        return self.elems[randint(0, self.n - 1)]
