# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # longest path in root.left and root.right
        # but it doesn;t have to pass the root 
        self.diameter = 0
        if not root:
            return 0
        def dfs(node):
            if not node:
                return 0
            maxL = dfs(node.left)
            maxR = dfs(node.right)
            self.diameter = max(self.diameter,maxL+maxR)
            return 1+max(maxL,maxR)
        dfs(root)
        return self.diameter
