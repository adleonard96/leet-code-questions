class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        n = str(n)
        product = int(n[0])
        sum_of_dig = int(n[0])

        for i in range(1, len(n)):
            product *= int(n[i]) 
            sum_of_dig += int(n[i]) 
        
        return product - sum_of_dig