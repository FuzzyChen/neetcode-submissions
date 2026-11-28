# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # return Boolean
        def dfs(node,low,high):
             # In order traverse
            if not node:
                return True
            
            if not low < node.val < high:
                return False

            validL = dfs(node.left,low,node.val)

            validR = dfs(node.right,node.val, high)

            return validL and validR
            
        return dfs(root,-float("inf"),float("inf"))