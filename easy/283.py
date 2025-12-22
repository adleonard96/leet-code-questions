class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left= 0 
        right = 0

        while right < len(nums):
            if nums[left] == 0:
                while nums[right] == 0:
                    right += 1
                    if right == len(nums):
                        break
                
                if right == len(nums):
                    break

                nums[left] = nums[right]
                nums[right] = 0

            left += 1
            if left > right:
                right = left 