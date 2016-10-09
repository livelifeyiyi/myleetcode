# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = fast = head
        while (fast and fast.next):
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = fast = head
        while True:
            if fast == None or fast.next == None: return None
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break

        fast = head
        while (fast != slow):
            slow = slow.next
            fast = fast.next
        return fast