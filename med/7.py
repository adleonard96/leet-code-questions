class Solution:
    def reverse(self, x: int) -> int:
        val = 0
        if x < 0:
            val = str(x)
            val = int(val[:0:-1]) * -1
        else:
            val = int(str(x)[::-1])

        if val > 2147483648 - 1 or val < -2147483648:
            return 0
        
        return val