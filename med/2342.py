class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        matches = defaultdict(list)
        for num in nums:
            num = str(num)
            total = 0
            for val in num:
                total += int(val)

            num = int(num)
            if total in matches and len(matches[total]) == 2:
                matches[total] = sorted(matches[total])
                if matches[total][0] < num:
                    matches[total][0] = num
            else:
                matches[total].append(num)
            
        res = -1

        for val in list(matches.values()):
            if len(val) == 2:
                res = max(res, val[0] + val[1])

        return res