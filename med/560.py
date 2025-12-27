class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        check = {0: 1}
        prefix = [nums[0]]
        ans = 0
        for i in range(1, len(nums)):
            prefix.append(prefix[-1] + nums[i])

        for num in prefix:
            if num - k in check:
                ans += check[num - k]
            
            if num in check:
                check[num] += 1
            else:
                check[num] = 1

        return ans