# -*- coding:utf-8 -*-

__author__ = [
    '"liubo" <liubo.cs@hotmail.com>'
]
'''
refer to https://discuss.leetcode.com/topic/16600/tree-deserializer-and-visualizer-for-python
'''


class TreeNode(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return 'TreeNode({})'.format(self.val)


def deserialize(string):
    if string == '{}':
        return None
    nodes = [None if val == 'null' else TreeNode(int(val))
             for val in string.strip('[]{}').split(',')]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids: node.left = kids.pop()
            if kids: node.right = kids.pop()
    return root


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def to_node_list(lst):
    head = None
    tmp = None
    for i in lst:
        if not head:
            head = ListNode(i)
            tmp = head
        else:
            tmp.next = ListNode(i)
            tmp = tmp.next
    return head


def to_list(head):
    if not head:
        return None
    tmp = head
    lst = []
    while tmp != None:

        lst.append(tmp.val)
        tmp = tmp.next
        if tmp == head:
            break
    return lst


def to_list_left(head):
    tmp = head
    lst = []
    while tmp != None:
        lst.append(tmp.val)
        tmp = tmp.left
        if tmp == head:
            break
    return lst


def to_list_right(head):
    tmp = head
    lst = []
    while tmp != None:
        lst.append(tmp.val)
        tmp = tmp.right
        if tmp == head:
            break
    return lst


def compare_list(l1, l2):
    if l1 == l2:
        return True


def drawtree(root):
    def height(root):
        return 1 + max(height(root.left), height(root.right)) if root else -1

    def jumpto(x, y):
        t.penup()
        t.goto(x, y)
        t.pendown()

    def draw(node, x, y, dx):
        if node:
            t.goto(x, y)
            jumpto(x, y - 20)
            t.write(node.val, align='center', font=('Arial', 12, 'normal'))
            draw(node.left, x - dx, y - 60, dx / 2)
            jumpto(x, y - 20)
            draw(node.right, x + dx, y - 60, dx / 2)

    import turtle
    t = turtle.Turtle()
    t.speed(0)
    turtle.delay(0)
    h = height(root)
    jumpto(0, 30 * h)
    draw(root, 0, 30 * h, 40 * h)
    t.hideturtle()
    turtle.mainloop()
