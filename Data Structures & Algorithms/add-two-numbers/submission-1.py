# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1:
            return l2
        if not l2:
            return l1
        n1 = n2 = 0
        #get the nums and add them
        
        count = 0
        while l1:
            n1 += l1.val * (10 ** count)
            count += 1
            l1 = l1.next
        count = 0
        while l2:
            n2 += l2.val * (10 ** count)
            count += 1
            l2 = l2.next
        num = n1 + n2
        # make a new link list from num
        dummy = ListNode(0)
        start = dummy
        while num >= 10:
            cur = num % 10 
            num = num //10
            start.next = ListNode(cur)
            start = start.next
        start.next = ListNode(num)
        return dummy.next
            

