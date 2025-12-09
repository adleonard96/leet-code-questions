class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        start = 0
        end = 1
        prev = None
        count = 0
        back_shift = 0

        for i in range(len(nums)):
            if prev is None:
                prev = nums[i]
                count += 1
                continue
            
            if back_shift > 0:
                nums[i - back_shift] = nums[i]

            if nums[i] == prev:
                count += 1


                if count > 2:
                    back_shift += 1

            else:
                prev = nums[i]
                count = 1

            
        
        return len(nums) - back_shift 