class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        self.res = False
        self.travel(root,subRoot)
        return self.res
    def travel(self,node,subNode):
        if not node or self.res:
            return
        
        q1 = deque([node])
        q2 = deque([subNode])
        match = True
        while q1 or q2:
            left = q1.popleft() if q1 else None
            right = q2.popleft() if q2 else None
            if left and right and left.val == right.val:
                q1.append(left.left)
                q1.append(left.right)
                q2.append(right.left)
                q2.append(right.right)
            elif left is None and right is None:
                continue
            else:
                match = False
                break
        if match:
            self.res = True
            return

        self.travel(node.left,subNode)
        self.travel(node.right,subNode)