from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        checker = defaultdict(int)
        max_len = 0 
        left = -1
        for i in range(len(s)):
            if s[i] in checker:
                left = checker[s[i]] if left < checker[s[i]] else left
            checker[s[i]] = i
            max_len = max(max_len,  i - left)

        return max_len