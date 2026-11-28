# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = -float("inf")

        def dfs(node): #return maxSum path with the Node
            if not node:
                return 0
            leftMax = max(dfs(node.left),0)
            rightMax= max(dfs(node.right),0)
            maxVal = node.val + max(leftMax , rightMax, 0) 
            self.res = max( self.res, node.val + leftMax + rightMax )
            return maxVal
        
        
        dfs(root)
        return self.res

