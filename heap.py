__author__ = [
    '"liubo" <liubo.cs@hotmail.com>'
]


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


heap = MaxHeap()
# print(heap.count())
# for num in [3, 9, 1, 2, 4, 5]:
#     heap.add(num)
# print(heap.val)
# print(heap.top())

import heapq

lst = [3, 2, 1, 5, 18, 2]
heapq.heapify(lst)

print(lst)


def y():
    yield [1, 2, 3]


for i in y():
    print(i)
