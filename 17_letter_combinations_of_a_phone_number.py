# -*- coding:utf-8 -*-
from typing import List

__author__ = [
    '"liubo" <liubo.cs@hotmail.com>'
]


class Solution:
    letter_dict = {
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"],
    }

    def letterCombinations(self, digits: str) -> List[str]:
        ret = []
        if digits:
            cur_digit = digits[0]
            for l in self.letter_dict[cur_digit]:
                if digits[1:]:
                    for sub in self.letterCombinations(digits[1:]):
                        ret.append(l + sub)
                else:
                    ret.append(l)
        return ret
