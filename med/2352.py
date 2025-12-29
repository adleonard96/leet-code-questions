from collections import defaultdict


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        c_check = defaultdict(list)
        total = 0
        r_check = defaultdict(list)
        for i in range(len(grid)):
            print(grid[i])
            for j in range(len(grid)):
                r_check[i].append(str(grid[i][j]))
                c_check[j].append(str(grid[i][j]))
        
        counter = defaultdict(int)
        for val in c_check.values():
            counter["".join(val)] += 1
            
        for val in r_check.values():
            if "".join(val) in counter:
                total += counter["".join(val)]
                
        return total
    
Solution().equalPairs([[3,2,1],[1,7,6],[2,7,7]])