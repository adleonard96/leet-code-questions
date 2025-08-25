class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        mapping = {}
        for i in range(len(heights)):
            if mapping.get(heights[i]):
                mapping[heights[i]].append(names[i])
            else:
                mapping[heights[i]] = [names[i]]
        
        sorted_heights = sorted(heights, reverse=True)
        ans = []
        for height in sorted_heights:
            for name in mapping.get(height):
                ans.append(name)

        return ans