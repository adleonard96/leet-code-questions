class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        highest = 0
        count = 0

        for num in nums:
            if num == 1:
                count += 1
            else:
                if count > highest:
                    highest = count
                count = 0
        
        if count > highest:
            highest = count

        return highest