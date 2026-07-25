# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        # BFS
        arr= deque([(root,-float('inf'))])
        res = 0
        while arr:
            for _ in range(len(arr)):
                node,maxVal = arr.popleft()
                if node.val >= maxVal:
                    res += 1
                if node.left:
                    arr.append((node.left,max(node.val,maxVal)))
                if node.right:
                    arr.append((node.right,max(node.val,maxVal)))
        return res
        