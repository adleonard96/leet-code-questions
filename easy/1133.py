from collections import defaultdict


class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        unique = sorted(list(set(nums)), reverse=True)
        count = defaultdict(int)
        
        for num in nums:
            count[num] += 1
            
        for num in unique:
            if count[num] == 1:
                return num
            
        return -1