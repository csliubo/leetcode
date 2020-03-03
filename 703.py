from typing import List

__author__ = [
    '"liubo" <liubo.cs@hotmail.com>'
]
'''
维护小顶堆，比堆顶元素大的进去
'''
import heapq


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.k = k
        for index, num in enumerate(nums):
            self.add(num)

    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        else:
            if val > self.heap[0]:
                heapq.heappop(self.heap)
                heapq.heappush(self.heap, val)
        return self.heap[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
