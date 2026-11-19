# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = node = ListNode(None)
        node1 = list1
        node2 = list2
        while node1 and node2:
            if  node1.val < node2.val:
                node.next = ListNode(node1.val,None)
                node = node.next
                node1 = node1.next
            else:
                node.next = ListNode(node2.val,None)
                node = node.next
                node2 = node2.next
        if node1:
            node.next = node1
        if node2:
            node.next = node2
        return dummy.next
        