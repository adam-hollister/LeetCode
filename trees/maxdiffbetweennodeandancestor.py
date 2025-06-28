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
Given the root of a binary tree, find the maximum value v 
for which there exist different nodes a and b where v = |a.val - b.val| and a is an ancestor of b.
A node a is an ancestor of b if either: any child of a is equal to b or any child of a is an ancestor of b.
"""
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def dfs(node: TreeNode, min_value , max_value) -> int:
            if node is None:
                return max_value - min_value

            min_value = min(node.val, min_value)
            max_value = max(node.val, max_value)

            left = dfs(node.left, min_value, max_value)
            right = dfs(node.right, min_value, max_value)

            return max(left, right)

        if not root:
            return 0

        ans = dfs(root, root.val, root.val)
        return ans

if __name__ == "__main__":
    sol = Solution()
    tree1 = build_tree([8,3,10,1,6,None,14,None,None,4,7,13])
    tree2 = build_tree([1,None,2,None,0,3])

    assert sol.maxAncestorDiff(tree1) == 7, "Test Case 1 Failed"
    assert sol.maxAncestorDiff(tree2) == 3, "Test Case 2 Failed"

    print("All test cases passed!")
