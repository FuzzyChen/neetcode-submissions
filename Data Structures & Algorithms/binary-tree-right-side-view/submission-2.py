# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # BTS
        if not root:
            return []
        arr = deque([root])
        res = []

        while arr:
            tempArr = []
            for _ in range(len(arr)):
                node = arr.popleft()
                if node.left:
                    arr.append(node.left)
                if node.right:
                    arr.append(node.right)
                tempArr.append(node.val)
            res.append(tempArr[-1])
        return res