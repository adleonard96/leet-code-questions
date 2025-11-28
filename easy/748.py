class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        shortest = ""
        unique = set(licensePlate.lower())
        for word in words:
            match = True
            for char in unique:
                if char.isdigit() or char == " ":
                    continue
                if char not in word.lower():
                    match = False
                    break
                if word.lower().count(char) < licensePlate.lower().count(char):
                    match = False
                    break

            if not match:
                continue
            
            if shortest == "" or len(word) < len(shortest):
                shortest = word

        return shortest
