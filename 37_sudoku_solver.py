# -*- coding:utf-8 -*-
import copy

__author__ = [
    '"liubo" <liubo.cs@hotmail.com>'
]


class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        self.ans = None
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        bulks = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val != ".":
                    bulk = (i // 3) * 3 + (j // 3)
                    rows[i].add(val)
                    cols[j].add(val)
                    bulks[bulk].add(val)
        self._dfs(board, rows, cols, bulks)

        for i in range(9):
            for j in range(9):
                board[i][j] = self.ans[i][j]

    def _dfs(self, board, rows, cols, bulks):
        bulk = row = col = None
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    row, col, bulk = i, j, (i // 3) * 3 + (j // 3)
        if row is None:
            self.ans = board
            return True
        available_nums = [str(i) for i in range(1, 10) if
                          str(i) not in rows[row] and str(i) not in cols[col] and str(i) not in bulks[bulk]]

        for num in available_nums:

            board[row][col] = num
            rows[row].add(num)
            cols[col].add(num)
            bulks[bulk].add(num)
            if self._dfs(board, rows, cols, bulks):
                return True
            else:
                board[row][col] = "."
                rows[row].remove(num)
                cols[col].remove(num)
                bulks[bulk].remove(num)
        return False

    def change(self, lst):
        lst[1] = 1
        print(lst)


s = Solution()
i = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]
print(4 // 3)
print(s.solveSudoku(i))
print(i)
