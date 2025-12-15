class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        count = 0
        current = []
        for price in prices:
            if current and current[-1] == price + 1:
                current.append(price)
            else:
                current = [price]
            
            count += len(current)

        return count