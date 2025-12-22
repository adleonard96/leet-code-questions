class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        prefix = [nums[0]]
        lowest = float('inf')

        for i in range(1, len(nums)):
            prefix.append(nums[i] + prefix[-1])

        for val in prefix:
            lowest = min(lowest, val)

        if lowest >= 1:
            return 1

        return abs(lowest) + 1