class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        left = 0
        right = k - 1
        vowels = ("a", "e", "i", "o", "u")
        current_vowel = 0
        for i in range(0, right + 1):
            if s[i] in vowels:
                current_vowel += 1

        max_vowels = current_vowel

        while right < len(s)-1:
            if s[left] in vowels:
                current_vowel -= 1
            left += 1
            right += 1
            if s[right] in vowels:
                current_vowel += 1
            
            max_vowels = max(max_vowels, current_vowel)

            if max_vowels == k:
                return max_vowels
        
        return max_vowels