# -*- coding:utf-8 -*-

__author__ = [
    '"liubo" <liubo.cs@hotmail.com>'
]


class LRUCache:
    class Node(object):
        def __init__(self, key, value, parent=None, child=None):
            self.parent = parent,
            self.child = child
            self.value = value
            self.key = key

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.tail, self.head = None, None

    def _move_node_to_head(self, node):
        if node != self.head:
            parent = node.parent
            if node.child:
                child = node.child
                child.parent = parent
                parent.child = child
            else:
                parent.child = None
                self.tail = parent
            current_head = self.head
            current_head.parent = node
            node.child = current_head
            self.head = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._move_node_to_head(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].value = value
            self._move_node_to_head(self.cache[key])
            return
        node = self.Node(key, value)
        self.cache[key] = node
        if not self.head:
            self.head, self.tail = node, node
            self.cache[key] = node
            return
        current_head = self.head
        current_head.parent = node
        node.child = current_head
        self.head = node
        if len(self.cache) > self.capacity:
            self.remove_tail()

    def remove_tail(self) -> None:
        tail_node = self.tail
        del self.cache[tail_node.key]
        self.tail = tail_node.parent
        self.tail.child = None


# Your LRUCache object will be instantiated and called as such:

capacity = 1
obj = LRUCache(capacity)
param_1 = obj.get(1)
obj.put(1, 2)
