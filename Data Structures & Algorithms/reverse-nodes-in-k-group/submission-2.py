# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        start = dummy

        cur = head
        arr = []
        while cur:
            arr.append(cur.val)
            cur = cur.next
        n = len(arr) // k
        m = len(arr) % k

        for i in range(n):
            par = arr[i*k:(i+1)*k]
            for val in par[::-1]:
                start.next = ListNode(val)
                start = start.next
        if m!=0:
            left = arr[n*k:]
            for val in left:
                start.next = ListNode(val)
                start = start.next
        return dummy.next

