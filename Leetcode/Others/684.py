class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        n: int = len(edges)  # there's only 1 extra edge so the number of nodes is the number of edges
        representatives: list[int] = [node for node in range(n + 1)]  # ignore index 0
        child_nums: list[int] = [1 for _ in range(n + 1)]

        def find_representative(node: int):
            cur_node: int = node
            while cur_node != representatives[cur_node]:
                representatives[cur_node] = representatives[representatives[cur_node]]
                cur_node = representatives[cur_node]
            return cur_node

        # return False if both nodes are in the same group and True otherwise
        def union(node1: int, node2: int) -> bool:
            node1_repr: int = find_representative(node1)
            node2_repr: int = find_representative(node2)

            if node1_repr == node2_repr:
                return False

            if child_nums[node1_repr] > child_nums[node2_repr]:
                representatives[node2] = node1_repr
                representatives[node2_repr] = node1_repr
                child_nums[node1_repr] += child_nums[node2_repr]
            else:
                representatives[node1] = node2_repr
                representatives[node1_repr] = node2_repr
                child_nums[node2_repr] += child_nums[node1_repr]
            return True

        for node1, node2 in edges:
            if not union(node1, node2):
                return [node1, node2]
