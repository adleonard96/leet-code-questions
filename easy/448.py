class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        filled = set(range(1, len(nums) + 1))
        nums_set = set(nums)
        return list(filled.difference(nums_set))