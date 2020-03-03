# -*- coding:utf-8 -*-
from typing import List

__author__ = [
    '"liubo" <liubo.cs@hotmail.com>'
]

import heapq


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []
        col = row = len(matrix)
        for i in range(row):
            for j in range(col):
                if i * row + j < k:
                    heapq.heappush(heap, -matrix[i][j])
                else:
                    if matrix[i][j] < -heap[0]:
                        heapq.heappop(heap)
                        heapq.heappush(heap, -matrix[i][j])
        return -heap[0]
