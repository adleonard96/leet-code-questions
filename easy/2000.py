class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        i = j = 0
        while j < len(word) and word[j] != ch:
            j += 1
        
        if j == len(word):
            return word

        word_list = list(word)
        while j > i:
            swap = word_list[j]
            word_list[j] = word_list[i]
            word_list[i] = swap
            j -= 1
            i += 1

        return "".join(word_list)
