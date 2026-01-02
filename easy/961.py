class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        checker = defaultdict(int)
        count_search = len(nums) / 2

        for num in nums:
            checker[num] += 1
            if checker[num] == count_search:
                return num