class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_vals = sorted(nums)
        ans = []
        for num in nums:
            ans.append(sorted_vals.index(num))

        return ans