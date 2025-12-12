class MinStack(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
      
        self.stack = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        if not self.stack:
            self.stack.append((val, val))
        else:
            current_min = self.stack[-1][1]
            self.stack.append((val, val if val < current_min else current_min))

    def pop(self):
        """
        :rtype: None
        """
        if self.stack:
            self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        if not self.stack:
            raise IndexError("top from empty MinStack")
        return self.stack[-1][0]

    def getMin(self):
        """
        :rtype: int
        """
        if not self.stack:
            raise IndexError("getMin from empty MinStack")
        return self.stack[-1][1]
