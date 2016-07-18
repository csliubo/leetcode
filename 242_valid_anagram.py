# -*- coding:utf-8 -*-

__author__ = [
    '"liubo" <liubo.cs@hotmail.com>'
]


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s == t:
            return True

        if not s or not t:
            return False

        if s.__len__() != t.__len__():
            return False

        dict_s = {}
        dict_t = {}

        for i in range(0, s.__len__()):
            ch = s[i]
            if ch in dict_s:
                dict_s[ch] += 1
            else:
                dict_s[ch] = 1

        for i in range(0, t.__len__()):
            ch = t[i]
            if ch in dict_t:
                dict_t[ch] += 1
            else:
                dict_t[ch] = 1

        if dict_s.__len__() != dict_t.__len__():
            return False

        for ch in dict_s:
            if dict_s.get(ch) != dict_t.get(ch, 0):
                return False
        return True


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        dict_s = {}
        dict_t = {}
