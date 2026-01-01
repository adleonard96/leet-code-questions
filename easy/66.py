from typing import List

def plusOne(digits: List[int]) -> List[int]:
    digits = map(lambda x: str(x), digits)
    digits = str(int("".join(digits)) + 1)
    return list(map(lambda x: int(x), list(digits)))

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0
        additional = 1
        for i in range(len(digits) -1 , -1, -1):
            curr = digits[i] + additional + carry
            if curr >= 10:
                digits[i] = curr % 10 
                carry = 1
            else:
                digits[i] = curr % 10 
                carry = 0
                break
            additional = 0
        
        if carry:
            return [1] + digits

        return digits