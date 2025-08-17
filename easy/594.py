class Solution:
    def findLHS(self, nums: List[int]) -> int:
        count = {}
        max_seq = 0
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1

        unique = set(nums)

        for num in unique:
            if num+1 in count:
                if count[num] + count[num+1] > max_seq:
                    max_seq = count[num] + count[num + 1]

        return max_seq