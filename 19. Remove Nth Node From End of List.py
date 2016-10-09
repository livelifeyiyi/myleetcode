# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        '''
        lens = len(head)
        renode = []
        for i in range(0,lens):
            if lens-i == n:
                #break
                continue
            else:
                renode.append(head[i])
        return renode
        '''
        self.next = head
        nodelist = [self]
        while head.next:
            if len(nodelist) == n:
                nodelist.pop(0)
            nodelist += head,
            head = head.next
        nodelist[0].next = nodelist[0].next.next
        return self.next
        '''self.n = n
        p = self.head
        length = 0
        while p!= 0:
            length +=1
            p = p.next
        post = self.head
        lengthn = length-self.n
        for i in range(0,lengthn):
            p = post
            post = post.next
            i += 1
        p.next = post.next
        return p
        '''
            
S = Solution()
print S.removeNthFromEnd(ListNode([1,2,3,4]),2)