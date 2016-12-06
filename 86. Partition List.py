import linkedList
class Solution(object):
	def partition(self, head, x):
		"""
		:type head: ListNode
		:type x: int
		:rtype: ListNode
		"""
		small = psmall = linkedList.ListNode(None)
		big = pbig = linkedList.ListNode(None)
		while head:
			if head.val >= x:
				pbig.next = head
				pbig = pbig.next
			if head.val < x:
				psmall.next = head
				psmall = psmall.next
			head = head.next
		pbig.next = None
		psmall.next = big.next
		return small.next


data = [1,4,3,2,5,2]
l = linkedList.LinkList()
head = l.initlist(data)
s = Solution()        
print s.partition(head, 3)