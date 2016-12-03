import linkedList
class Solution(object):
	def rotateRight(self, head, k):
		"""
		:type head: ListNode
		:type k: int
		:rtype: ListNode
		"""
		if not head: return None
		n = self.getlength(head)
		if k >= n: k = k % n
		if head.next == None or k == 0:
			return head
		fast = slow = head
		for i in range(0,k):
			fast = fast.next
		if not fast: return head
		while fast.next:
			fast = fast.next
			slow = slow.next
		end = slow.next
		p = end
		slow.next = None
		while end and end.next:
			end = end.next
		end.next = head
		return p

	def getlength(self, head):
		p = head
		length = 0
		while p:
			length += 1
			p = p.next
		return length

data = [1,2]
l = linkedList.LinkList()
head = l.initlist(data)
s = Solution()
print s.rotateRight(head, 3)