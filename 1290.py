import math

from utils import to_node_list, to_list, ListNode

__author__ = [
    '"liubo" <liubo.cs@hotmail.com>'
]


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        if not head:
            return 0

        def cal_single_bit(node):
            val, factor = node.val, 1
            if node.next:
                ret_val, ret_factor = cal_single_bit(node.next)
                factor = ret_factor + factor
                if val:
                    val = 2 ** (factor - 1) + ret_val
                else:
                    val = ret_val
            return val, factor

        num, _ = cal_single_bit(head)
        return num


if __name__ == "__main__":
    s = Solution()
    l1 = to_node_list([1, 0, 1])
    print(s.getDecimalValue(l1))
    l1 = to_node_list([1])
    print(s.getDecimalValue(l1))
    l1 = to_node_list([0])
    print(s.getDecimalValue(l1))
    l1 = to_node_list([])
    print(s.getDecimalValue(l1))
    l1 = to_node_list([1, 1, 1])
    print(s.getDecimalValue(l1))
    l1 = to_node_list([0, 1, 1])
    print(s.getDecimalValue(l1))
