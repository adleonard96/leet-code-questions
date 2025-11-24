class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        operation_count = 0

        for num in nums:
            if num % 3 == 0:
                continue
            operation_count += 1

        return operation_count