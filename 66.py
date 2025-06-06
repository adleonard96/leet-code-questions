from typing import List

def plusOne(digits: List[int]) -> List[int]:
    digits = map(lambda x: str(x), digits)
    digits = str(int("".join(digits)) + 1)
    return list(map(lambda x: int(x), list(digits)))

print(plusOne([1,2,3]))