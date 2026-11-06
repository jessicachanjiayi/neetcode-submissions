# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Base Case
        if not root:
            return 0
        # Recursion
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        # We use DFS+Recursion, firstly we check whether the root is available, then we do recursion on every node. let it pick the larger depth between its left side and right side subtrees. The time complexity is O(n)