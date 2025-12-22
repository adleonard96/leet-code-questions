class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left = 0
        right = k - 1
        ans = float('-inf')

        sum = 0
        for i in range(0, k):
            sum += nums[i]

        while right < len(nums): 
            ans = max(ans, sum/k)
            sum -= nums[left]
            left += 1
            right += 1
            if right < len(nums):
                sum += nums[right]


        return ans 
    
sol = Solution().findMaxAverage([-1], 1)