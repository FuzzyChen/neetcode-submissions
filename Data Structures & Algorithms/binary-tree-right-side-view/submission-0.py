# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #BFS
        if not root:
            return []
        arr = deque([root])
        res = []
        while arr:
            tmp = []
            for _ in range(len(arr)):
                pop = arr.popleft()
                tmp.append(pop.val)
                if pop.left:
                    arr.append(pop.left)
                if pop.right:
                    arr.append(pop.right)
            res.append(tmp[-1])
        return res
        