class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        total = left = right = 0
        min_length = float("inf")

        while left < len(nums):
            while total >= target:
                min_length = min(min_length, right - left)
                total -= nums[left]
                left += 1

            if right < len(nums):
                total += nums[right]
                right += 1
            else:
                break

        if min_length == float("inf"):
            return 0
        return min_length