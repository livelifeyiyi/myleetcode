import linkedList
class Solution(object):
	def isPalindrome(self, head):
		"""
        :type head: ListNode
        :rtype: bool
        """
		if not head: return True
		val = []
		p = head
		while p:
			val.append(p.val)
			p = p.next
		half = len(val)/2
		for i in range(0, half):
			if val[i] == val[-i-1]:
				continue
			else:
				return False
		return True
	def isPalindrome2(self, head):

		slow = fast = cur = head
		while fast and fast.next:
			slow = slow.next
			fast = fast.next.next

		slowval = [slow.val]
		while slow.next:
			slow = slow.next
			slowval.append(slow.val)
		while slowval:
			if slowval.pop() == cur.val:
				cur = cur.next
				continue
			else: return False
		return True

data = [1,2,3,2,1]
list = linkedList.LinkList()
head = list.initlist(data)
S = Solution()
print S.isPalindrome2(head)