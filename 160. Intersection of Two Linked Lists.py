import linkedList
import gc
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
        gc.collect()
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
        gc.collect()
        a, b = headA, headB
        if lena > lenb:
            for i in range(0, lena-lenb):
                a = a.next
        if lenb >lena:
            for i in range(0, lenb-lena):
                b = b.next
        #while a.next and b.next and a.val != b.val:
        if a != b:
            a = a.next
            b = b.next
        return a
        #if a.val != b.val and not a.next and not b.next:
        #    return None
        #else: return a
L = linkedList.LinkList()
dataa = [1,3,5,7,9]
datab = [9]
headA = L.initlist(dataa)
headB = L.initlist(datab)
S = Solution2()
print S.getIntersectionNode2(headA, headB)