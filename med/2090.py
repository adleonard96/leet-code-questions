class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        prefix = [nums[0]]

        for i in range(1, len(nums)):
            prefix.append(prefix[-1] + nums[i])

        if len(nums) / 2 < k:
            return [-1] * len(nums) 
        ans = [-1] * k

        for i in range(k, len(nums) - k):
            right = prefix[i + k]
            left = 0
            if i - k > 0:
                left = prefix[i - k - 1]

            ans.append(int((right - left)/(k * 2 + 1)))
            
        ans += [-1] * k
        return ans
    
Solution().getAverages([7,4,3,9,1,8,5,2,6], 3)