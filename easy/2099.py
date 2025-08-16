class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        vals = sorted(nums, reverse=True)
        vals = vals[:k]
        ans = []
        count = {}
        for val in vals:
            if val in count:
                count[val] += 1
            else:
                count[val] = 1

        for num in nums: 
            if num in count:
                if count[num] > 0:
                    count[num] -= 1
                    ans.append(num)
                
            if len(ans) == k:
                return ans