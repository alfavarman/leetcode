"""
Given a string s, find the length of the longest substring  without repeating characters.
Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding window algorithm
        window = ''
        max_l = 0
        start = 0

        # loop through the string s and add each char to the window
        for end in range(len(s)):
            while s[end] in window:
                start += 1
                window = window[start:]

            window += s[end]

            max_l = max(max_l, len(window))
        return max_l





        # if the key already exists in the window, update the value to +1
        # if value is move then one start reduce most left element of the window






        # max_l store max len of window




s = "abcabcbb"
print(Solution().lengthOfLongestSubstring(s))