# -*- coding:utf-8 -*-

__author__ = [
    '"liubo" <liubo.cs@hotmail.com>'
]

FORWARD = 1
MISMATCH = -1
CONTINUE = 0
FORWARD_AND_STOP = 2
CHAR_DOT = '.'
CHAR_STAR = '*'


class State(object):
    def match(self, ch):
        pass

    def __repr__(self):
        if hasattr(self, 'ch'):
            return "%s: %s" % (self.__class__.__name__, self.ch)
        return self.__class__.__name__


class SingleCharState(State):
    def __init__(self, ch):
        self.ch = ch

    def match(self, ch):
        if self.ch == ch:
            return FORWARD
        else:
            return MISMATCH


class MultipleCharState(State):
    def __init__(self, ch):
        self.ch = ch

    def match(self, ch):
        if self.ch == ch:
            return CONTINUE
        else:
            return FORWARD_AND_STOP


class AnythingState(State):
    def __init__(self):
        pass

    def match(self, ch):
        return CONTINUE


class AnyCharState(State):
    def __init__(self, ch):
        self.ch = ch

    def match(self, ch):
        return FORWARD


class Solution(object):
    def match_test(self, s, states):
        # print s, states
        state_len = states.__len__()
        state_index = 0

        ch_index = 0
        str_len = s.__len__()
        while (ch_index < str_len):
            ch = s[ch_index]
            if state_index >= state_len:
                return False
            current_state = states[state_index]
            result = current_state.match(ch)

            if result == FORWARD:
                state_index += 1
            elif result == CONTINUE:
                # 尝试最小匹配
                # pass
                if ch_index < str_len and state_index < state_len - 1:
                    if self.match_test(s[ch_index:], states[state_index + 1:]):
                        return True
            elif result == FORWARD_AND_STOP:
                state_index += 1
                ch_index -= 1
            else:
                return False
            ch_index += 1

        # 匹配完
        # print state_index
        # print ch_index, state_index, state_len, states[state_index:], states
        if state_index < state_len:
            # 没有匹配完,但后面的状态都是0-n的,也是可以
            for state in states[state_index:]:
                if type(state) not in [MultipleCharState, AnythingState]:
                    return False
        return True

    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if not s and not p:
            return True
        if not p:
            return False

        states = self.parse_pattern(p)
        if not s:
            for state in states:
                if type(state) not in [MultipleCharState, AnythingState]:
                    return False
        return self.match_test(s, states)

    def parse_pattern(self, p):
        len = p.__len__()
        states = []
        # state 可以进行合并

        last_state = None
        for i in range(0, len):
            current_char = p[i]
            if current_char == CHAR_STAR:
                continue
            next_char = p[i + 1] if i + 1 < len else None
            if current_char == CHAR_DOT:
                if next_char and next_char == CHAR_STAR:
                    current_state = AnythingState()
                else:
                    current_state = AnyCharState(current_char)
            else:
                if next_char and next_char == CHAR_STAR:
                    current_state = MultipleCharState(current_char)
                else:
                    current_state = SingleCharState(current_char)
            if last_state:
                # 合并规则
                last_state_type = type(last_state)
                current_state_type = type(current_state)

                if last_state_type == current_state_type:
                    if last_state_type == AnythingState:
                        current_state = None
                    elif last_state_type == MultipleCharState and last_state.ch == current_state.ch:
                        current_state = None
            if current_state:
                last_state = current_state
                states.append(current_state)
        print states
        return states


s = Solution()
# print s.isMatch("aaa", "a*a")
# print s.isMatch("aaa", "aa")
# print s.isMatch("aaa", "aaaa")
# print s.isMatch("", "")
# print s.isMatch("a", "")
# print s.isMatch("", "a")
# print s.isMatch("ab", ".*c")
# print s.isMatch("aab", "c*a*b")
# print s.isMatch("bbbba", ".*a*a")
# print s.isMatch("ba", ".*a")
# print s.isMatch("aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*c")
print s.isMatch("b", "c*bb")
print s.isMatch("abcaaaaaaabaabcabac", ".*ab.a.*a*a*.*b*b*")
