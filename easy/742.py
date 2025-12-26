class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix = [nums[0]]
        left_sum = 0
        for i in range(1, len(nums)):
            prefix.append(prefix[-1] + nums[i])

        res = -1

        for i in range(len(prefix)):
            if left_sum == prefix[-1] - prefix[i]:
                return i
            left_sum = prefix[i]

        return res