class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        letter_map = {}
        s = s.split(" ")

        if len(s) != len(pattern):
            return False
            
        for i in range(len(pattern)):
            if letter_map.get(s[i]):
                if letter_map.get(s[i]) != pattern[i]:
                    return False
            else:
                if pattern[i] in letter_map.values():
                    return False
                letter_map[s[i]] = pattern[i]

        return True