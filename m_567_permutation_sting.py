"""567. Permutation in String
Medium
9.9K
317
Companies
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

 

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false
 

Constraints:

1 <= s1.length, s2.length <= 104
s1 and s2 consist of lowercase English letters.
"""

from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        p = 0
        e = len(s1)
        s1_c = Counter(s1)
        
        for _ in range(len(s1), len(s2)+1):
            window = Counter(s2[p:e])
            if all(window.get(key, 0) >= count for key, count in s1_c.items()):
                return True
            p += 1
            e += 1
        
        return False



class Solution1:
    def checkInclusion(self, s1: str, s2: str) -> bool:    
        d1 = {c:0 for c in string.ascii_lowercase}
        d2 = {c:0 for c in string.ascii_lowercase}

        for n in s1:
            d1[n] +=1
        for m in s2[:len(s1)]:
            d2[m] +=1

        if(d1 == d2):
            return True

        for j in range(len(s1),len(s2)):
            d2[s2[j]]+=1
            d2[s2[j-len(s1)]]-=1
            if(d1 == d2):
                return True
        
        return False



s1 = "adc"

s2 = "dcda"


print(Solution().checkInclusion(s1=s1, s2=s2))