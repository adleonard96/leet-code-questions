class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        check = {}

        for c in s:
            if c in check:
                check[c] += 1
            else:
                check[c] = 1

        count = check[s[0]]
        for c in check.keys():
            if check[c] != count:
                return False

        return True