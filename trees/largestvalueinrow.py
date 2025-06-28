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
Given the root of a binary tree, return an array of the largest value in each row of the tree.
"""
class Solution:
    def largestvalueinrows(self, root: Optional[TreeNode]) -> list[int]:
        if not root:
            return []

        ans = []
        queue = deque([root])
        while queue:
            row_size = len(queue)
            largest = float("-inf")
            for _ in range(row_size):
                node = queue.popleft()
                largest = max(node.val, largest)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(largest)
            x = 1
        return ans

if __name__ == "__main__":
    sol = Solution()
    tree1 = build_tree([1,2,3,4,5])

    assert sol.largestvalueinrows(tree1) == [1,3,5], "Test Case 1 Failed"

    print("All test cases passed!")
