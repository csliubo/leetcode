from utils import ListNode, to_node_list, to_list

__author__ = [
    '"liubo" <liubo.cs@hotmail.com>'
]


class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        if not head:
            return None

        # convert to array
        cur = head
        current_sum = 0
        pre_sum_index = {}
        while cur:
            current_sum += cur.val
            pre_sum_index[current_sum] = cur
            cur = cur.next

        if pre_sum_index.get(0):
            head = pre_sum_index[0].next
        cur = head
        current_sum = 0
        while cur:
            current_sum += cur.val
            if current_sum in pre_sum_index:
                cur.next = pre_sum_index[current_sum].next
            cur = cur.next
        return head


if __name__ == "__main__":
    l1 = to_node_list([1, 2, -3, 3, 1])

    s = Solution()
    print(to_list(s.removeZeroSumSublists(l1)))
    l1 = to_node_list([])
    print(to_list(s.removeZeroSumSublists(l1)))
