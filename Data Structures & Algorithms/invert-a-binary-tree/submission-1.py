# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Use DFS and Recursion to deal with this case. First we see whether the root is null. Then we define a function to swap the left children and right children of the root. After we recursively apply the same function to both the left and right subtrees. 
        if not root:
            return None
        
        temp = root.left
        root.left = root.right
        root.right = temp
        # Create a temp to store the value so it can be fixed

        self.invertTree(root.left)
        self.invertTree(root.right)
        # Recursively call dfs on the new left child and right child

        return root
            
        
        
        