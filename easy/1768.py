class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        alternate = ""
        while i < len(word1) and i < len(word2):
            alternate += word1[i]
            alternate += word2[i]
            i += 1
        
        while i < len(word1):
            alternate += word1[i]
            i+= 1
        
        while i < len(word2):
            alternate += word2[i]
            i+= 1

        return alternate