# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        node = head
        while node:
            arr.append(node.val)
            node = node.next
        d1 = ListNode()
        d2 = d1
        for v in arr[::-1]:
            d2.next = ListNode(v)
            d2 = d2.next
        return d1.next
