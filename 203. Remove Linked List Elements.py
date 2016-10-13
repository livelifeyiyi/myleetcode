# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class LinkList(object):
	def __init__(self):
		self.head = 0
	def initlist(self, data):
		self.head = ListNode(data[0])
		p = self.head
		for i in data[1:]:
			node = ListNode(i)
			p.next = node
			p = p.next
		return self.head

class Solution(object):
	def removeElements(self, head, val):
		"""
		:type head: ListNode
		:type val: int
		:rtype: ListNode
		"""
		dummy = ListNode(None)
		dummy.next = head
		node = dummy

		while node.next:
			if node.next.val == val:
				if node.next.next:
					node.next = node.next.next
				else: node.next = None
			else: node = node.next
		return dummy.next
	def removeElements2(self, head, val):
		node = head
		if not node: return head
		if not node.next:
			if node.val != val:
				return head
			else:
				return ListNode(None).next
		while node.next:
			if node.next.val == val:
				if node.next.next:
					node.next = node.next.next
				else:
					node.next = None
			else:
				node = node.next
		return head.next	#lack one element
data = [1,1,2]
l = LinkList()
head = l.initlist(data)
S = Solution()
print S.removeElements(head, 2)