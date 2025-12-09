class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:

        if len(nums) == 1:
            return True

        finished = True
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                finished = False
                break

        if not finished:
            finished = True
            for i in range(1, len(nums)):
                if nums[i] < nums[i - 1]:
                    finished = False
                    break

        return finished