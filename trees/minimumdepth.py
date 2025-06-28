# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
from typing import List
from typing import Optional

def build_tree(nodes: List[Optional[int]]) -> Optional[TreeNode]:
    if not nodes:
        return None

    root = TreeNode(nodes[0])
    queue = deque([root])
    i = 1

    while queue and i < len(nodes):
        current = queue.popleft()

        if i < len(nodes) and nodes[i] is not None:
            current.left = TreeNode(nodes[i])
            queue.append(current.left)
        i += 1

        if i < len(nodes) and nodes[i] is not None:
            current.right = TreeNode(nodes[i])
            queue.append(current.right)
        i += 1

    return root

"""
Given a binary tree, find its minimum depth.
The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
Note: A leaf is a node with no children.
"""
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(node, count):
            if node is None:
                return float("inf")

            count += 1

            if node.left is None and node.right is None:
                return count

            left = dfs(node.left, count)
            right = dfs(node.right, count)
            return min(left, right)
        if not root:
            return 0

        return dfs(root, 0)

if __name__ == "__main__":
    sol = Solution()
    tree1 = build_tree([3, 9, 20, None, None, 15, 7])
    tree2 = build_tree([2, None, 3, None, 4, None, 5, None, 6])

    assert sol.minDepth(tree1) == 2, "Test Case 1 Failed"
    assert sol.minDepth(tree2) == 5, "Test Case 2 Failed"

    print("All test cases passed!")
