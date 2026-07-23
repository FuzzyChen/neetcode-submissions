# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        #BFS
        arr = deque([root])
        res = []
        while arr:
            tmp = []
            tmpL = len(arr)
            for _ in range(tmpL):
                #something
                pop = arr.popleft()
                tmp.append(pop.val)
                if pop.left:
                    arr.append(pop.left)
                if pop.right:
                    arr.append(pop.right)
            res.append(tmp)
        return res
        