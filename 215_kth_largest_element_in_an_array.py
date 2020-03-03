# -*- coding:utf-8 -*-
from typing import List

__author__ = [
    '"liubo" <liubo.cs@hotmail.com>'
]

'''
也可以用堆来解决，建一个k个元素的最小堆，比堆顶元素大的就进去，同时堆顶pop出来
'''
import heapq
class Solution:
    def findKthLargest1(self, nums: List[int], k: int) -> int:
        return sorted(nums, reverse=True)[k - 1]

    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums[:k]
        heapq.heapify(heap)
        for num in nums[k:]:
            if num > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap,num)
        return heap[0]
