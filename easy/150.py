class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count = {}
        for letter in magazine:
            if count.get(letter):
                count[letter] += 1
            else:
                count[letter] = 1

        for letter in ransomNote:
            if count.get(letter) and count.get(letter) > 0:
                count[letter] -= 1
            else:
                return False


        return True