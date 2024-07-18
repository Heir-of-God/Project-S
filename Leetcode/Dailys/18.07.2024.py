# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        q, visited = deque(), set()
        visited_leaves = set()

        def count_leaves(leaf: TreeNode) -> None:
            nonlocal q, visited, res
            q.append([leaf, 1])

            while q:
                cur_node, cur_level = q.popleft()
                visited.add(cur_node)

                if cur_level > distance + 1:  # if we exceeded depth
                    break

                if cur_node in nodes_parents and nodes_parents[cur_node] not in visited:
                    q.append([nodes_parents[cur_node], cur_level + 1])

                if [cur_node.left, cur_node.right] == [None, None]:
                    if cur_node not in visited_leaves:  # if this is leaf we haven't counted
                        res += 1
                    continue

                if cur_node.left and cur_node.left not in visited:
                    q.append([cur_node.left, cur_level + 1])

                if cur_node.right and cur_node.right not in visited:
                    q.append([cur_node.right, cur_level + 1])

            q.clear()
            visited.clear()

        res = 0
        nodes_parents: dict[TreeNode, TreeNode] = {}  # TreeNode -> TreeNode (its parent)
        queue: list[TreeNode] = [root]

        while queue:
            node: TreeNode = queue.pop()

            if node.right:
                nodes_parents[node.right] = node
                queue.append(node.right)

            if node.left:
                nodes_parents[node.left] = node
                queue.append(node.left)

            if [node.left, node.right] == [None, None]:
                visited_leaves.add(node)
                count_leaves(node)

        return res
