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
data = [1,1,2]
l = LinkList()
head = l.initlist(data)