# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
from typing import List, Any
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
Given the root of a binary tree, return the sum of values of its deepest leaves.
"""
class Solution:
    def deepestleavessum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = deque([root])
        row_sum = 0
        while queue:
            row_length = len(queue)
            row_sum = 0
            for _ in range(row_length):
                node = queue.popleft()
                row_sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return row_sum
if __name__ == "__main__":
    sol = Solution()
    tree1 = build_tree([1,2,3,4,5,None,6,7,None,None,None,None,8])
    tree2 = build_tree([6,7,8,2,7,1,3,9,None,1,4,None,None,None,5])

    assert sol.deepestleavessum(tree1) == 15, "Test Case 1 Failed"
    assert sol.deepestleavessum(tree2) == 19, "Test Case 2 Failed"

    print("All test cases passed!")
