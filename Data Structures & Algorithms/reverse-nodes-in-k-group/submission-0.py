# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        arr = []
        dummy = ListNode(0)
        cur = dummy
        while head:
            arr.append(head.val)
            head = head.next

        for i in range(0,len(arr),k):
            group = arr[i:i+k]

            if len(group) ==k:
                group.reverse()
            for val in group:
                cur.next = ListNode(val)
                cur = cur.next
        return dummy.next