class Queue(object):
	def __init__(self):
		"""
		initialize your data structure here.
		"""
		self.queue = []
		self.poper = []

	def push(self, x):
		"""
		:type x: int
		:rtype: nothing
		"""
		self.queue.append(x)

	def pop(self):
		"""
		:rtype: nothing
		"""
		if not self.poper:
			while self.queue:
				self.poper.append(self.queue.pop())
		self.poper.pop()

	def peek(self):
		"""
		:rtype: int
		"""
		if self.poper:
			return self.poper[-1]
		return self.queue[0]

	def empty(self):
		"""
		:rtype: bool
		"""
		return len(self.poper) == 0 and len(self.queue) == 0
