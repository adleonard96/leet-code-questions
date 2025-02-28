class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums = sorted(nums)
        if nums[0] != 0:
            return 0

        current = 0

        for i in range(1, len(nums)):
            if nums[i] != current + 1:
                return current + 1

            current = nums[i]

        return len(nums)

