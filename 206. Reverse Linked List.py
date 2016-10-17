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
	def reverseList(self, head):
		if not head or not head.next:
			return head
		pre = next = ListNode(None)
		pre = pre.next
		while head:
			next = head.next
			head.next = pre
			pre = head
			head = next
		return pre
data = [1,2,3,4]
l = LinkList()
head = l.initlist(data)
s = Solution()
print s.reverseList(head)