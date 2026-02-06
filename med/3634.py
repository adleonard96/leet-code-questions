class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        vals = sorted(nums)

        removed = 0

        while vals and vals[0] * k < vals[-1]:
            if 
            vals.pop()
            removed += 1

        return removed
    
Solution().minRemoval([1,34,23], 2)


"""Not finished - realized the problem could remove elements from either side which then requires sliding window"""