# -*- coding:utf-8 -*-
from typing import List

__author__ = [
    '"liubo" <liubo.cs@hotmail.com>'
]


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        row = len(triangle)
        path_count = [x for x in triangle[row - 1]]
        for i in range(row - 2, -1, -1):
            for j in range(0, i + 1):
                path_count[j] = min(path_count[j], path_count[j + 1]) + triangle[i][j]
        return path_count[0]


s = Solution()
r = s.minimumTotal([[2]])
print(r)
for i in range(0):
    print("aaa")

