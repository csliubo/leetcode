# -*- coding:utf-8 -*-
import copy

__author__ = [
    '"liubo" <liubo.cs@hotmail.com>'
]


class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.ans = []
        self._dfs([], n)
        return [["." * i + "Q" + "." * (n - i - 1) for i in row] for row in self.ans]
        # for ans in self.ans:
        #     text_img = []
        #     for position in ans:
        #         row = ""
        #         for i in range(0, n):
        #             row += "." if i != position else "Q"
        #         text_img.append(row)
        #     ret.append(text_img)
        # return ret

    def _dfs(self, positions, left):
        if left == 0:
            self.ans.append(positions)
            return
        current_row = len(positions)
        total_col = len(positions) + left
        unused_positions = set()
        for index, position in enumerate(positions):
            row_diff = current_row - index
            unused_positions.add(position)
            unused_positions.add(row_diff + position)
            unused_positions.add(position - row_diff)
        for col in [x for x in range(total_col) if x not in unused_positions]:
            self._dfs(positions + [col], left - 1)


s = Solution()
r = s.solveNQueens(8)
print(len(r))
for img in r:
    # print(img)
    for row in img:
        print(row)
