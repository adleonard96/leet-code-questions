class Solution:
    def repeatedCharacter(self, s: str) -> str:
        ans = set()

        for letter in s:
            if letter in ans:
                return letter
            ans.add(letter)