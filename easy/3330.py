class Solution:
    def possibleStringCount(self, word: str) -> int:
        counts = {}
        sol = 1
        multiples = []
        last_letter = ""

        for char in word:
            if char != last_letter:
                last_letter = char
                continue
            if char in counts:
                counts[char] += 1
            else:
                counts[char] = 2
                
            if char not in multiples:
                multiples.append(char)

        for mult in multiples:
            sol += counts[mult] - 1

        return sol
    
sol = Solution()

sol.possibleStringCount("abbcccc")