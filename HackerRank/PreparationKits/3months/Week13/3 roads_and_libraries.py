import os


class UnionFind:
    def __init__(self, n: int) -> None:
        self.representatives: list[int] = [i for i in range(n + 1)]
        self.ranks: list[int] = [1 for _ in range(n + 1)]

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


def roadsAndLibraries(n: int, c_lib: int, c_road: int, cities: list[list[int]]) -> int:
    if c_lib <= c_road:
        return n * c_lib

    uf = UnionFind(n)
    for node1, node2 in cities:
        uf.union(node1, node2)

    res = 0
    counted = set()
    for node in range(1, n + 1, 1):
        representative = uf.find_representative(node)
        if representative not in counted:
            counted.add(representative)
            res += (uf.get_rank(representative) - 1) * c_road + c_lib

    return res


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")
    q = int(input().strip())
    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()
        n = int(first_multiple_input[0])
        m = int(first_multiple_input[1])
        c_lib = int(first_multiple_input[2])
        c_road = int(first_multiple_input[3])
        cities = []
        for _ in range(m):
            cities.append(list(map(int, input().rstrip().split())))
        result = roadsAndLibraries(n, c_lib, c_road, cities)
        fptr.write(str(result) + "\n")
    fptr.close()
