class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.mini = None

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        if self.mini is None:
            self.mini = x
        elif x < self.mini:
            self.mini = x


    def pop(self):
        """
        :rtype: void
        """
        x = self.stack.pop()
        if self.stack == []:
            self.mini = None
        elif self.mini == x:
            self.mini = min(self.stack)

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        min = self.stack
        min.sort()
        return min[0]"""

        return self.mini




obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
param_2 = obj.getMin()
obj.pop()
param_3 = obj.top()
param_4 = obj.getMin()
print param_2, param_3, param_4