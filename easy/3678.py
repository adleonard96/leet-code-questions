class Solution:
    def smallestAbsent(self, nums: List[int]) -> int:
        sum_of_num = 0

        for num in nums:
            sum_of_num += num

        average = 0
        if sum_of_num > 0:
            average = sum_of_num / len(nums)
        else:
            average = sum_of_num * len(nums)

        nums_larger = list(filter(lambda x: x > average, nums))
        
        found = False
        current = int(average) + 1
        while not found:
            if current not in nums_larger:
                if current <= 0:
                    current = 1
                    continue
                return current
            current += 1
