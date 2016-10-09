# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        point = head = ListNode(None)
        if l1 == None: return l2
        if l2 == None: return l1
        while(l1 and l2):
            if l1.val <= l2.val:
                point.next = l1
                l1 = l1.next
            elif l1.val > l2.val:
                point.next = l2
                l2 = l2.next
            point = point.next
        if l1:
            point.next = l1
        if l2:
            point.next = l2
        return head.next
        '''
        OR:
        head = ListNode(None)
        
        if l1 == None: return l2
        if l2 == None: return l1
        if l1.val <= l2.val:
            head = l1
            l1 = l1.next
        else: 
            head = l2
            l2 = l2.next
        point = head
        while(l1 and l2):
            if l1.val <= l2.val:
                point.next = l1
                l1 = l1.next
            elif l1.val > l2.val:
                point.next = l2
                l2 = l2.next
            point = point.next
        if l1:
            point.next = l1
        if l2:
            point.next = l2
        return head
        '''
S = Solution()
print S.mergeTwoLists([1],[2])