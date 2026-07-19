# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        arr1, arr2 = [],[]
        num1, num2 = 0,0
        while l1:
            arr1.append(l1.val)
            l1= l1.next
        while l2:
            arr2.append(l2.val)
            l2 = l2.next
        for i,digit in enumerate(arr1):
            num1 += digit * (10 ** i)
        for i,digit in enumerate(arr2):
            num2 += digit * (10 ** i)
        res = num1 + num2

        
        dummy = ListNode(-1)
        node = dummy
        for digit in reversed(str(res)):
            node.next = ListNode(int(digit))
            node = node.next
        return dummy.next

            
        