# -*- coding:utf-8 -*-

__author__ = [
    '"liubo" <liubo.cs@hotmail.com>'
]


class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.list = []
        self._dfs_gen(n, n, "")
        return self.list

    def _dfs_gen(self, left, right, current_str):
        if left == 0 and right == 0:
            self.list.append(current_str)
            return
        if left:
            self._dfs_gen(left - 1, right, current_str + "(")
        if right and right > left:
            self._dfs_gen(left, right - 1, current_str + ")")


s = Solution()
r = s.generateParenthesis(3)
print(r)
enumerate