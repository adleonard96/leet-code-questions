class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(" ")

        for i in range(len(words)):
            word_list = list(words[i])
            word_list.reverse()
            words[i] = "".join(word_list)
        
        return " ".join(words)