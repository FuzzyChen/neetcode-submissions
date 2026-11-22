"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        oldToNew = {}
        cur = head
        cur2 = head
        while cur:
            oldToNew[cur] = Node(cur.val)
            cur = cur.next
        #handle random and next
        while cur2:
            oldToNew[cur2].next = oldToNew.get(cur2.next)
            oldToNew[cur2].random  = oldToNew.get(cur2.random)
            cur2 = cur2.next
        return oldToNew[head]
