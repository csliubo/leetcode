from utils import deserialize, drawtree, to_list, to_list_left, to_list_right

__author__ = [
    '"liubo" <liubo.cs@hotmail.com>'
]


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def to_list(self, head):
        tmp = head
        lst = []
        while tmp != None:
            lst.append(tmp.val)
            tmp = tmp.next
        return lst

    def treeToDoublyList1(self, root: 'Node') -> 'Node':
        '''
        解法1，比较暴力的直接遍历存起来，然后直接按顺序调整指针即可，最后一步调整一下头节点和尾节点
        :param root:
        :return:
        '''
        if not root:
            return None
        ret = []

        def convert(node):
            nonlocal ret
            if node.left:
                convert(node.left)
            ret.append(node)
            if node.right:
                convert(node.right)

        convert(root)
        # if len(ret) == 1:
        #     return root
        for i in range(1, len(ret)):
            ret[i - 1].right = ret[i]
            ret[i].left = ret[i - 1]
        ret[0].left = ret[-1]
        ret[-1].right = ret[0]
        return ret[0]

    def treeToDoublyList(self, root: 'Node') -> 'Node':
        '''
        解法2，遍历的时候同时调整指针，这种应该是比较符合出题人的意图
        :param root:
        :return:
        '''
        if not root:
            return None
        head = root
        tail = root

        def traverse(node, direction, near_min=None, near_max=None):
            left_node, right_node = None, None
            if direction == -1 and not near_min and not node.left:
                nonlocal head
                head = node
            if direction == 1 and not near_max and not node.right:
                nonlocal tail
                tail = node

            if node.left:
                traverse(node.left, -1, near_min=near_min, near_max=node)
            elif near_min:
                node.left, near_min.right = near_min, node
            if node.right:
                traverse(node.right, 1, near_min=node, near_max=near_max)
            elif near_max:
                node.right, near_max.left = near_max, node

            return node

        traverse(root, 0)
        head.left = tail
        tail.right = head
        return head


root = deserialize('[4,2,5,1,3]')
s = Solution()

print(s.treeToDoublyList(root))
root = deserialize('[null]')
print(s.treeToDoublyList(root))

root = deserialize('[27,-99,55,null,-34,null,58,null,-8,null,59,null,8,null,68]')
# drawtree(root)
# print(to_list(root))
print(to_list_right(s.treeToDoublyList(root)))
