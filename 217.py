class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        set_of_nums = set(nums)

        return len(nums) != len(set_of_nums)