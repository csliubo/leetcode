# -*- coding:utf-8 -*-

__author__ = [
    '"liubo" <liubo.cs@hotmail.com>'
]


class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        if not board:
            return 0
        count = 0
        outter_len = board.__len__()
        inner_len = board[0].__len__()
        for i in range(0, outter_len):
            for j in range(0, inner_len):
                ch = board[i][j]
                if ch == "X":
                    if i > 0:
                        if board[i - 1][j] == "X":
                            continue
                    if j > 0:
                        if board[i][j - 1] == "X":
                            continue
                    count += 1
        return count


case = ["X..X", "...X", "...X"]


def convert(lst):
    lst = []
    for c in case:
        sub_lst = []
        for ch in c:
            sub_lst.append(ch)
        lst.append(sub_lst)
    return lst


print convert(case)

s = Solution()
print s.countBattleships(convert(case))
