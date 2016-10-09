# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        self.next = head
        #nodelist = [self]
        while( head and head.next):
            a = head.val
            head.val = head.next.val
            head.next.val = a
            head = head.next.next
        return self.next