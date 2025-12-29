from collections import defaultdict


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count = defaultdict(int)

        for c in text:
            count[c] += 1

        ans = 0
        isFormable = True
        while isFormable:
            enough_b = count["b"] >= 1
            enough_a = count["a"] >= 1
            enough_l = count["l"] >= 2
            enough_o = count["o"] >= 2
            enough_n = count["n"] >= 1

            if enough_b and enough_a and enough_l and enough_o and enough_n:
                ans += 1
                count["b"] -= 1
                count["a"] -= 1
                count["l"] -= 2
                count["o"] -= 2
                count["n"] -= 1
            else:
                return ans
