import linkedList
class Solution(object):
	def sortList(self, head):
		"""
		:type head: ListNode
		:rtype: ListNode
		"""
		return self.mergeSort(head)
		
	def mergeList(self, l, r):
		if not l: return r
		if not r: return l
		res = ListNode(-1)
		new = res
		while l and r:
			if l.val < r.val:
				new.next = l
				new = new.next
				l = l.next
			else:
				new.next = r
				new = new.next
				r = r.next
		if r:
			new.next = r
		if l:
			new.next = l
		return res.next
	def getMiddle(self, head):
		slow = fast = head
		while fast and fast.next:
			slow = slow.next
			fast = fast.next.next
		return slow
	def mergeSort(self, head):
		if not head or not head.next:
			return head

		mid = self.getMiddle(head)
		nextPart = None
		if mid:
			nextPart = mid.next
			mid.next = None
		return self.mergeList(self.mergeSort(head), self.mergeSort(nextPart))


class Solution2(object):
	def sortList(self, head):
		val = []
		h = head
		while h:
			val.append(h.val)
			h = h.next
		val.sort()
		h1 = head
		count = 0
		while h1:
			h1.val = val[count]
			count += 1
			h1 = h1.next
		return head

class Solution3(object):
	def sortList(self, head):
		def sort(head, until=None):
            '''
            Sort the list from head until `until`.
            '''
            if head == until:
                return head
            dummy = ListNode(None)
            dummy.next = head

            pivot = head.val
            smaller = dummy
            equal = dummy.next
            while equal.next not in (None, until) and equal.next.val == equal.val:
                equal = equal.next
            prev = equal
            p = prev.next
            while p not in (None, until):
                if p.val < pivot:
                    prev.next = p.next
                    p.next = smaller.next
                    smaller.next = p
                    smaller = p
                elif p.val == pivot and equal.next != p:
                    prev.next = p.next
                    p.next = equal.next
                    equal.next = p
                    equal = p
                else:
                    prev = p
                p = prev.next

            dummy.next = sort(dummy.next, smaller.next)
            equal.next = sort(equal.next, until)
            return dummy.next

        return sort(head)


data = [5,2,4,6,1,3,7]
l = linkedList.LinkList()
head = l.initlist(data)
s = Solution()
print s.sortList(head)