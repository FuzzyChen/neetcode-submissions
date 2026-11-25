# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        #loop through the 
        dummy = ListNode(0)
        arr = []
        for node in lists:
            while node:
                arr.append(node.val)
                node = node.next
        arr.sort()
        start = dummy
        for val in arr:
            start.next = ListNode(val)
            start = start.next
        return dummy.next