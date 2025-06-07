def mySqrt(x: int) -> int:
    if x == 1 or x == 2 or x == 3:
            return 1
    if x == 0:
        return 0
    mid = x // 2
    for i in range(mid + 2):
        if i * i > x:
            return i - 1
        elif i * i == x:
            return i
        
print(mySqrt(5))