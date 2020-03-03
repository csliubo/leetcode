# -*- coding:utf-8 -*-

__author__ = [
    '"liubo" <liubo.cs@hotmail.com>'
]


class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        row_count = len(board)

        bulks = [set() for _ in range(row_count)]
        cols = [set() for _ in range(row_count)]
        rows = [set() for _ in range(row_count)]

        for i in range(0, row_count):
            for j in range(0, row_count):
                v = board[i][j]
                if v != ".":
                    if v in rows[i] or v in cols[j] or v in bulks[int(i / 3) * 3 + int(j / 3)]:
                        return False
                    rows[i].add(v)
                    cols[j].add(v)
                    bulks[int(i / 3) * 3 + int(j / 3)].add(v)

        return True

    def _valid_row(self, row):
        if row:
            s = set()
            for n in [num for num in row if num != "."]:
                if n in s:
                    return False
                s.add(n)
        return True


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
print(s.isValidSudoku(i))
