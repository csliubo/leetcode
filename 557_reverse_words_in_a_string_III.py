# -*- coding:utf-8 -*-

__author__ = [
    '"liubo" <liubo.cs@hotmail.com>'
]


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        temp_word = ""
        ret = ""
        for ch in s:
            if ch != ' ':
                temp_word += ch
            else:
                ret += temp_word[::-1]
                ret += ' '
                temp_word = ""
        if temp_word:
            ret += temp_word[::-1]
        return ret

s = Solution()
print s.reverseWords("Let's take LeetCode contest")