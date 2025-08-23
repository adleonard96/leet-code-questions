class Solution:
    def similarPairs(self, words: List[str]) -> int:
        sets = []
        pairs = 0
        for word in words:
            key = "".join(sorted(list(set(word))))
            if key in sets:
                pairs += len(list(filter(lambda x: x == key, sets)))
            
            sets.append(key)

        return pairs 