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
Given the root of a binary tree, return the length of the diameter of the tree.
The diameter of a binary tree is the length of the longest path between any two nodes in a tree. 
This path may or may not pass through the root.
The length of a path between two nodes is represented by the number of edges between them.
"""
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0
        def dfs(node: TreeNode) -> int:
            if node is None:
                return 0
            #go as far left as possible
            left = dfs(node.left)
            #come up 1 and try to go right
            right = dfs(node.right)

            #nodes logic begins
            self.max_diameter = max(left+right, self.max_diameter) #left + right is the diameter through that node
            #node returns height to the parent
            return 1 + max(left, right) #left, right, self and this is your height

        dfs(root)
        return self.max_diameter

if __name__ == "__main__":
    sol = Solution()
    tree1 = build_tree([1,2,3,4,5])
    tree2 = build_tree([1,2])
    tree3 = build_tree([])

    assert sol.diameterOfBinaryTree(tree1) == 3, "Test Case 1 Failed"
    assert sol.diameterOfBinaryTree(tree2) == 1, "Test Case 2 Failed"
    assert sol.diameterOfBinaryTree(tree3) == 0, "Test Case 2 Failed"

    print("All test cases passed!")
