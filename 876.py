from utils import ListNode, to_node_list, to_list

__author__ = [
    '"liubo" <liubo.cs@hotmail.com>'
]


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        # 快慢指针
        if not head:
            return None
        if not head.next:
            return head
        slow, fast = head, head.next
        while fast.next:
            slow = slow.next
            if fast.next.next:
                fast = fast.next.next
            else:
                return slow
        return slow.next


if __name__ == "__main__":
    s = Solution()
    l1 = to_node_list([1, 2, 3, 4, 2, 1])
    print(to_list(s.middleNode(l1)))
    l1 = to_node_list([1, 2, 3, 2, 1])
    print(to_list(s.middleNode(l1)))
    l1 = to_node_list([1])
    print(to_list(s.middleNode(l1)))
    l1 = to_node_list([1,1])
    print(to_list(s.middleNode(l1)))