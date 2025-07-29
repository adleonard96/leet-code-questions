class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        letter_map = {}
        for i in range(len(s)):
            if letter_map.get(s[i]):
                if letter_map.get(s[i]) != t[i]:
                    return False
            else:
                if t[i] in letter_map.values():
                    return False
                letter_map[s[i]] = t[i]

        return True
    
    
sos = Solution()

sos.isIsomorphic('badc', 'baba')