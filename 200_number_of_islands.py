# -*- coding:utf-8 -*-
import dis
from typing import List

__author__ = [
    '"liubo" <liubo.cs@hotmail.com>'
]


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        row = len(grid)
        col = len(grid[0])
        root = [[None for _ in range(col)] for _ in range(row)]
        self.count = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] != "0":
                    root[i][j] = (i, j)
                    self.count += 1

        def find(i, j):
            root_i, root_j = i, j

            while (root_i, root_j) != root[root_i][root_j]:
                root_i, root_j = root[root_i][root_j]

            tmp_i, tmp_j = i, j
            while (tmp_i, tmp_j) != root[tmp_i][tmp_j]:
                (tmp_i, tmp_j), root[tmp_i][tmp_j] = root[tmp_i][tmp_j], (root_i, root_j)
            return (root_i, root_j)

        def merge(i1, j1, i2, j2):
            root_i1, root_j1 = find(i1, j1)
            root_i2, root_j2 = find(i2, j2)

            if (root_i1, root_j1) != (root_i2, root_j2):
                root[root_i2][root_j2] = (root_i1, root_j1)
                self.count -= 1

        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1":
                    if i > 0 and grid[i - 1][j] == "1":
                        merge(i - 1, j, i, j)
                    if j > 0 and grid[i][j - 1] == "1":
                        merge(i, j - 1, i, j)

        return self.count


# [[(2, 0), (0, 0), (0, 0)], [None, (0, 0), None], [(2, 0), (2, 0), (2, 0)]]
# [[(2, 0), (0, 0), (0, 0)], [None, (0, 0), None], [(2, 0), (0, 0), (2, 0)]]

#
s = Solution()
# print(s.numIslands(
#     [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]))
# islands = [["1", "1", "0", "0", "0"],
#            ["1", "1", "0", "0", "0"],
#            ["0", "0", "1", "0", "0"],
#            ["0", "0", "0", "1", "1"]]
#
# print(s.numIslands(islands))
islands = [["1", "1", "1"],
           ["0", "1", "0"],
           ["1", "1", "1"]]
print(s.numIslands(islands))

i = [[1], [2], [3]]
tmp, i[0] = i[0], i[1]
# dis.dis("tmp, i[0] = i[0], i[1]")
print(tmp, i[0])
i = [[1], [2], [3]]
i[0], tmp = i[1], i[0]
# dis.dis("i[0], tmp = i[1], i[0]")
print(tmp, i[0])

x = 17
print(x & (-x))


def f(s):
    print(s)
    return 0


sum(map(f, ["傻逼"]*100000))
