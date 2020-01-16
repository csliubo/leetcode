# -*- coding:utf-8 -*-

__author__ = [
    '"liubo" <liubo.cs@hotmail.com>'
]


class Stack(object):
    def __init__(self):
        self._lst_ = []

    def push(self, x):
        self._lst_.append(x)

    def pop(self):
        if self._lst_:
            return self._lst_.pop()
        return None

    def peek(self):
        if self._lst_:
            len = self._lst_.__len__()
            return self._lst_[len - 1]
        return None

    def is_empty(self):
        return self._lst_.__len__() == 0

    def __repr__(self):
        if self.is_empty():
            return "[]"
        else:
            return self._lst_.__repr__()


class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = Stack()
        self.head = None

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        if self.empty():
            self.head = x
        self.stack.push(x)

    def pop(self):
        """
        :rtype: nothing
        """
        if self.stack.is_empty():
            return None
        # print self.stack
        new_stack = Stack()
        while not self.stack.is_empty():
            new_stack.push(self.stack.pop())
        # print new_stack
        x = new_stack.pop()
        self.head = new_stack.peek()
        while not new_stack.is_empty():
            self.stack.push(new_stack.pop())
        return x

    def peek(self):
        """
        :rtype: int
        """
        return self.head

    def empty(self):
        """
        :rtype: bool
        """
        return self.stack.is_empty()


q = Queue()
print q.peek()
print q.pop()
print q.empty()
q.push(1)

# print q.pop()
print q.empty()
q.push(2)
print q.peek()
q.push(3)

print q.pop()
print q.peek()
# print q.pop()
# print q.empty()
# print q.pop()
