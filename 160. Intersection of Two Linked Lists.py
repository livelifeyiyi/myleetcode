# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#Memory Limit Exceeded
class Solution1(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None
        a,b = headA, headB
        while a!= b:
            a = a.next if a else headB
            b = b.next if b else headA
        return a

class Solution2(object):
    def getIntersectionNode(self, headA, headB):
        if not headA or not headB:
            return None
        a, b = headA, headB
        lena, lenb = 0, 0
        while a:
            a = a.next
            lena += 1
        while b:
            b = b.next
            lenb += 1
        a, b = headA, headB
        if lena > lenb:
            for i in range(0, lena-lenb):
                a = a.next
        if lenb >lena:
            for i in range(0, lenb-lena):
                b = b.next
        while a != b:
            a = a.next
            b = b.next
        return a