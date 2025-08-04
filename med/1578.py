class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        prev_color = colors[0]
        time_needed = 0
        i = 0
        j = 1
        while j < len(colors):
            while colors[j] == colors[i]:
                if neededTime[j] < neededTime[i]:
                    time_needed += neededTime[j]
                    j += 1
                else:
                    time_needed += neededTime[i]
                    i = j
                    j += 1
                
                if j == len(colors):
                    break
            
            i = j
            j += 1
    
        return time_needed