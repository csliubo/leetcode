__author__ = [
    '"liubo" <liubo.cs@hotmail.com>'
]


class MyLinkedList:
    class ListNode:
        def __init__(self, x):
            self.val = x
            self.next = None

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._head = None
        self._element_count = 0

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        cur = self._head
        while index:
            if not cur:
                return -1
            cur = cur.next
            index -= 1
        return cur.val if cur else -1

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        node = self.ListNode(val)
        node.next = self._head
        self._head = node

        self._element_count += 1

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        if not self._head:
            self.addAtHead(val)
        else:
            cur = self._head
            while cur.next:
                cur = cur.next
            cur.next = self.ListNode(val)
            self._element_count += 1

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index > self._element_count:
            return
        elif index == self._element_count:
            self.addAtTail(val)
        else:
            if index == 0:
                self.addAtHead(val)
            else:
                prev, cur = None, self._head
                while index:
                    prev, cur, index = cur, cur.next, index - 1
                node = self.ListNode(val)
                node.next = cur
                prev.next = node
                self._element_count += 1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index >= self._element_count:
            return

        self._element_count -= 1
        if index == 0:
            self._head = self._head.next
        else:
            prev, cur = None, self._head
            while index:
                prev, cur, index = cur, cur.next, index - 1
            if cur:
                prev.next = cur.next
            else:
                prev.next = None


obj = MyLinkedList()
param_1 = obj.get(1)
obj.addAtHead(2)
obj.addAtTail(3)
obj.addAtIndex(1, 2)
obj.deleteAtIndex(1)
