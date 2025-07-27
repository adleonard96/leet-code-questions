# Took the no brain solution to the problem, if the max number was 1000 the solution wouldn't work.
# “I choose a lazy person to do a hard job. Because a lazy person will find an easy way to do it.” ― Bill Gates

class Solution:
    def smallestNumber(self, n: int) -> int:
        if n > 511:
            return 1023
        elif n > 255:
            return 511
        elif n > 127:
            return 255
        elif n > 63: 
            return 127
        elif n > 31:
            return 63
        elif n > 15:
            return 31
        elif n > 7:
            return 15
        elif n > 3:
            return 7
        elif n > 1:
            return 3
        else:
            return 1