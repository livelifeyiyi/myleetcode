# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
	def deleteDuplicates(self, head):
		"""
		:type head: ListNode
		:rtype: ListNode
		"""
		#if head == None:
		#	return head
		current = head
		while current:
			while current.next and current.val == current.next.val:
			 	current.next = current.next.next
			current = current.next
		return head