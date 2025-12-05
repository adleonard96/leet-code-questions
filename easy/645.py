class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        missing = -1
        duplicate = -1
        vals = {}
        check = 1
        nums = sorted(nums)

        for num in nums:
            if check not in nums:
                missing = check
            if num not in vals:
                vals[num] = 1
            else:
                duplicate = num
            if duplicate != -1 and missing != -1:
                return [duplicate, missing]
            check += 1

        return [duplicate, nums[len(nums) - 1] + 1]