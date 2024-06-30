class UnionFind:
    def __init__(self, n: int) -> None:
        self.n: int = n
        self.representatives: list[int] = [i for i in range(n + 1)]
        self.children_num: list[int] = [1 for _ in range(n + 1)]
        self.can_traverse = False

    def can_traverse_full(self) -> bool:
        return self.can_traverse

    def find_representative(self, node: int) -> int:
        cur_node: int = node
        while cur_node != self.representatives[cur_node]:
            self.representatives[cur_node] = self.representatives[self.representatives[cur_node]]
            cur_node = self.representatives[cur_node]
        return cur_node

    # returns False if this edge is unnecessary and True otherwise
    def union(self, node1: int, node2: int):
        node1_repr: int = self.find_representative(node1)
        node2_repr: int = self.find_representative(node2)

        if node1_repr == node2_repr:
            return False

        if self.children_num[node1_repr] > self.children_num[node2_repr]:
            self.representatives[node2] = node1_repr
            self.representatives[node2_repr] = node1_repr
            self.children_num[node1_repr] += self.children_num[node2_repr]
            if self.children_num[node1_repr] == self.n:
                self.can_traverse = True
        else:
            self.representatives[node1] = node2_repr
            self.representatives[node1_repr] = node2_repr
            self.children_num[node2_repr] += self.children_num[node1_repr]
            if self.children_num[node2_repr] == self.n:
                self.can_traverse = True
        return True


class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: list[list[int]]) -> int:
        alice_uf = UnionFind(n)
        bob_uf = UnionFind(n)
        can_delete = 0

        for edge_type, node1, node2 in edges:
            if edge_type == 3:
                bob_need: bool = bob_uf.union(node1, node2)
                alice_need: bool = alice_uf.union(node1, node2)
                can_delete += not bob_need and not alice_need

        for edge_type, node1, node2 in edges:
            if edge_type == 3:
                continue

            bob_need = False
            if edge_type == 2:
                bob_need = bob_uf.union(node1, node2)
            alice_need = False
            if edge_type == 1:
                alice_need = alice_uf.union(node1, node2)
            can_delete += not bob_need and not alice_need

        return -1 if False in (alice_uf.can_traverse_full(), bob_uf.can_traverse_full()) else can_delete
