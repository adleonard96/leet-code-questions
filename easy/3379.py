class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        length = len(nums)
        result = [0] * length
        for i, num in enumerate(nums):
            if num > 0:
                index = i + num
                if index >= length: # 1 2 0 1 2
                    index =  index % length 
                result[i] = nums[index]
            elif num < 0:
                index = i - abs(num)
                while index < 0:
                    index += 1
                    index = length - 1 - abs(index)
                result[i] = nums[index]
            else:
                result[i] = num
        
        return result
    