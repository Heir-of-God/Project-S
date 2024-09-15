import os


class UnionFind:
    def __init__(self, n: int) -> None:
        self.representatives: list[int] = [i for i in range(n)]
        self.ranks: list[int] = [1 for _ in range(n)]

    def find_representative(self, node: int) -> int:
        while node != self.representatives[node]:
            node, self.representatives[node] = (
                self.representatives[node],
                self.representatives[self.representatives[node]],
            )
        return node

    def get_rank(self, node: int) -> int:
        return self.ranks[self.find_representative(node)]

    def union(self, node1: int, node2: int) -> None:
        repr1: int = self.find_representative(node1)
        repr2: int = self.find_representative(node2)

        if repr1 != repr2:
            if self.ranks[repr1] >= self.ranks[repr2]:
                self.ranks[repr1] += self.ranks[repr2]
                self.representatives[repr2] = repr1
                self.representatives[node2] = repr1
            else:
                self.ranks[repr2] += self.ranks[repr1]
                self.representatives[repr1] = repr2
                self.representatives[node1] = repr2


def journeyToMoon(n: int, astronaut: list[list[int]]) -> int:
    uf = UnionFind(n)
    for id1, id2 in astronaut:
        uf.union(id1, id2)

    counted = set()
    country_counts = []
    for person in range(n):
        representative = uf.find_representative(person)
        if representative not in counted:
            counted.add(representative)
            country_counts.append(uf.get_rank(representative))

    s = sum(country_counts)
    res = 0
    for n in country_counts:
        res += n * (s - n)

    return res // 2  # we count each pair twice


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    p = int(first_multiple_input[1])
    astronaut = []
    for _ in range(p):
        astronaut.append(list(map(int, input().rstrip().split())))
    result = journeyToMoon(n, astronaut)
    fptr.write(str(result) + "\n")
    fptr.close()
