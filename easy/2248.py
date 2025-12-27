class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        nums_dict = {}

        for num in nums:
            for val in num:
                if val in nums_dict:
                    nums_dict[val] += 1
                else:
                    nums_dict[val] = 1

        ans = []
        num_arr = len(nums)
        for num in nums_dict.keys():
            if  nums_dict[num] == num_arr:
                ans.append(num)

        return sorted(ans) 
