from typing import Optional, List
from collections import defaultdict

# Define a  binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        # Use defaultdict for more efficient dictionary operations
        children_hashmap = defaultdict(lambda: [None, None])
        children_set = set()

        # Construct children_hashmap and children_set
        for parent, child, isleft in descriptions:
            children_set.add(child)
            target = 0 if isleft else 1
            children_hashmap[parent][target] = child

        # Find the root node (node that is not a child)
        root_val = next(parent for parent in children_hashmap if parent not in children_set)

        # Use inner function to construct the tree
        def construct_tree(cur_node_val):
            new_node = TreeNode(cur_node_val)
            if cur_node_val in children_hashmap:
                left_child, right_child = children_hashmap[cur_node_val]
                if left_child is not None:
                    new_node.left = construct_tree(left_child)
                if right_child is not None:
                    new_node.right = construct_tree(right_child)
            return new_node

        return construct_tree(root_val)
