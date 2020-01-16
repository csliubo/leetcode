# -*- coding:utf-8 -*-

__author__ = [
    '"liubo" <liubo.cs@hotmail.com>'
]


class Solution(object):
    rows = {
        "q": 1,
        "w": 1,
        "e": 1,
        "r": 1,
        "t": 1,
        "y": 1,
        "u": 1,
        "i": 1,
        "o": 1,
        "p": 1,
        "a": 2,
        "s": 2,
        "d": 2,
        "f": 2,
        "g": 2,
        "h": 2,
        "j": 2,
        "k": 2,
        "l": 2,
        "z": 3,
        "x": 3,
        "c": 3,
        "v": 3,
        "b": 3,
        "n": 3,
        "m": 3
    }

    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        ret = []
        for word in words:
            if self.in_same_row(word.lower()):
                ret.append(word)
        return ret

    def in_same_row(self, word):

        last_row_no = self.rows[word[0]]
        for ch in word[1:]:
            row_no = self.rows[ch]
            if row_no != last_row_no:
                return False
        return True


s = Solution()
print s.findWords(["Hello", "Alaska", "Dad", "Peace"])
