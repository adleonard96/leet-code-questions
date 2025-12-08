import math

class Solution:
    def countTriples(self, n: int) -> int:
        triples = []
        nums = [i for i in range(n+1) ]
        for i in range(1, n+1):
            for j in range(1, n + 1):
                if i == j:
                    continue
                val = math.sqrt(i**2 + j**2)
                if val in nums:
                    triples.append([i, j, val])

        return len(triples) 
