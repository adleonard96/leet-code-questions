class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        prefix = [0]
        longest = 0
        track = defaultdict(list)
        for i in range(len(nums)):
            if nums[i] == 0:
                prefix.append(prefix[-1] - 1)
            else:
                prefix.append(prefix[-1] + 1)

        for i in range(len(prefix)):
            if len(track[prefix[i]]) > 0:
                longest = max(longest, i - track[prefix[i]][0])
            track[prefix[i]].append(i)

        return longest
    
# could be optimized to use 1 loop