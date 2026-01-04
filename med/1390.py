import math


class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        ans = 0

        for num in nums:
            curr = set()
            for i in range(1, int(math.sqrt(num)) + 1):
                if (num / i) % 1 == 0:
                    curr.add(i)
                    curr.add(num / i)
                    if len(curr) > 4:
                        break
            
            if len(curr) == 4:
                for val in curr:
                    ans += val

        return int(ans)
    
Solution().sumFourDivisors([1,2,3,4,5,6,7,8,9,10])