# Backspace String Compare
# Given two strings S and T, 
# return if they are equal when both are typed into empty text editors. 
# # means a backspace character.

class Solution(object):  # Time complexity O(M+N), space complexity O(M+N) 
    def backspaceCompare(self, S, T):
        def build(S):
            tmp = []
            for c in S:
                if c != "#":
                    tmp.append(c)
                elif tmp:  # if I set this line as 'else:' or 'elif c=="#", then when the tmp list is empty, raise error.
                    tmp.pop()
            return "".join(tmp)
        return build(S) == build(T)