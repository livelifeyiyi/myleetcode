# Definition for singly-linked list.
#class ListNode(object):
#     def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(-1)
        current = head
        carry = 0
        while l1 is not None or l2 is not None or carry != 0:
            a = 0
            if l1 is not None:
                a = l1.val
                l1 = l1.next
            b = 0
            if l2 is not None:
                b = l2.val
                l2 = l2.next
            x = a + b + carry
            if x >= 10:
                x -= 10
                carry = 1
            else:
                carry = 0
            current.next = ListNode(x)
            current = current.next
        return head.next