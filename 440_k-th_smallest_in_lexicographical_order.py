# -*- coding:utf-8 -*-

__author__ = [
    '"liubo" <liubo.cs@hotmail.com>'
]


class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        cur = 1
        k -= 1
        while k > 0:
            first, last, step = cur, cur + 1, 0
            while first <= n:
                step += min(n + 1, last) - first
                print(step, last, first)
                first *= 10
                last *= 10
            if step <= k:
                k -= step
                cur += 1
            else:
                k -= 1
                cur *= 10

        return cur


class MaxHeap(object):

    def __init__(self, compare_func=None):
        self.val = []
        self.compare_func = compare_func

    def add(self, element):
        last_index = len(self.val)
        self.val.append(element)
        while last_index > 0:
            parent_index = (last_index - 1) // 2
            if self.compare_func:
                if self.compare_func(self.val[last_index], self.val[parent_index]) > 0:
                    self.val[last_index], self.val[parent_index] = self.val[parent_index], self.val[last_index]
                else:
                    break
            else:
                if self.val[last_index] > self.val[parent_index]:
                    self.val[last_index], self.val[parent_index] = self.val[parent_index], self.val[last_index]
                else:
                    break
            last_index = parent_index

    def top(self):
        return self.val[0] if self.val else None

    def count(self):
        return len(self.val)

    def remove_top(self):
        if not self.val:
            return
        self.val[0], self.val[-1] = self.val[-1], self.val[0]
        del self.val[-1]
        if not self.val:
            return
        count = len(self.val)
        cur_index = 0
        while (cur_index * 2 + 1) < count:
            left_index, right_index = cur_index * 2 + 1, cur_index * 2 + 2
            max_child_index = left_index
            if right_index < count and self.compare_func(self.val[left_index], self.val[right_index]) < 0:
                max_child_index = right_index
            if self.compare_func(self.val[max_child_index], self.val[cur_index]):
                self.val[cur_index], self.val[max_child_index] = self.val[max_child_index], self.val[cur_index]
            else:
                break
            cur_index = max_child_index

    def replace_top(self, num):
        if not self.val:
            return
        self.val[0] = num
        count = len(self.val)
        cur_index = 0
        while (cur_index * 2 + 1) < count:
            left_index, right_index = cur_index * 2 + 1, cur_index * 2 + 2
            max_child_index = left_index
            if right_index < count and self.compare_func(self.val[left_index], self.val[right_index]) < 0:
                max_child_index = right_index
            if self.compare_func(self.val[cur_index], self.val[max_child_index]) < 0:
                self.val[cur_index], self.val[max_child_index] = self.val[max_child_index], self.val[cur_index]
                cur_index = max_child_index
            else:
                break


class Trie(object):

    def __init__(self):
        self.is_num = False
        self.child = [None] * 10

    def add(self, num):
        node = self
        print(num)
        for ch in str(num):

            index = ord(ch) - ord('0')
            if not node.child[index]:
                print(index, num)
                node.child[index] = Trie()
            else:
                print("hit")
            node = node.child[index]
        node.is_num = True


s = Solution()
import cProfile

l = s.findKthNumber(100, 26)
print(l)
# print(s.findKthNumber(999999, 3))
