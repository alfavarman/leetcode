"""
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the

characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).



Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false


Constraints:

0 <= s.length <= 100
0 <= t.length <= 104
s and t consist only of lowercase English letters.


Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk where k >= 109, and you want to check one by one
 to see if t has its subsequence. In this scenario, how would you change your code?
"""

s = "abc"
t = "ahbgdc"


def isSubsequence(s: str, t: str) -> bool:
    stack_s = [*s]
    for i in t:
        if len(stack_s) == 0:
            return True
        if i == stack_s[0]:
            stack_s.pop(0)

    return True if len(stack_s) == 0 else False




# FASTES
# class Solution:
#     def isSubsequence(self, s: str, t: str) -> bool:
#         if len(s) > len(t):
#             return False
#         elif s == t:
#             return True
#         s_l_index = 0
#         for i in s:
#             if i in t[s_l_index:]:
#                 t = t[t[s_l_index:].index(i)+1:]
#             else:
#                 return False
#         return True
print(isSubsequence(s, t))