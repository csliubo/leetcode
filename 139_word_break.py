# -*- coding:utf-8 -*-

__author__ = [
    '"liubo" <liubo.cs@hotmail.com>'
]


class Solution:
    # @param s, a string
    # @param wordDict, a set<string>
    # @return a boolean
    _cache_ = set()

    def wordBreak(self, s, wordDict):
        print s
        print wordDict
        print "========"
        self._cache_ = set()
        self._no_word_ = set()
        if self.quickCheck(s, wordDict):
            return self.wordBreak2(s, wordDict)
        else:
            return False

    def wordBreak2(self, s, wordDict):
        # print "in word break 2", s
        if s in self._cache_:
            return True
        if s in self._no_word_:
            return False
        len = s.__len__()
        index = 1
        mark_position = []
        while index <= len:
            if s[:index] in wordDict:
                if index == len:
                    return True
                else:
                    mark_position.append(index)
                    self._cache_.add(s[:index])
                    print "add cache", index
            index += 1
        # print mark_position
        # print s.__len__()
        if not mark_position:
            return False
        for pos in mark_position:
            word = s[pos:]
            if self.wordBreak2(word, wordDict):
                self._cache_.add(word)
                print self._cache_
                return True
            else:
                self._no_word_.add(word)
        # exit(0)
        return False

    def quickCheck(self, s, wordDict):

        word_chars = set()
        for word in wordDict:
            for char in word:
                word_chars.add(char)

        for c in s:
            if c not in word_chars:
                return False
        return True


s = Solution()
# print s.wordBreak("ab", ["a", "b"])
# print s.wordBreak("a", ["a", "b"])
# print s.wordBreak("cars", ["car", "ca", "rs"])
print s.wordBreak(
    "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab",
    ["a", "aa", "ba"])
