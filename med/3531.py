class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        x_vals = {}
        y_vals = {}
        covered = []
        
        for building in buildings:
            if building[0] in x_vals:
                x_vals[building[0]].append(building)
            else:
                x_vals[building[0]] = [building]
            if building[1] in y_vals:
                y_vals[building[1]].append(building)
            else:
                y_vals[building[1]] = [building]
        
        for key in y_vals.keys():
            y_vals[key] = sorted(y_vals[key], key=lambda x: x[0])
        
        for key in x_vals.keys():
            buildings = sorted(x_vals[key], key=lambda x: x[1])
            
            for i in range(1, len(buildings) - 1):
                y = buildings[i][1]
                x = buildings[i][0]
                if y_vals[y][0][0] != x and y_vals[y][-1][0] != x:
                    covered.append(buildings[i])
                    
        return len(covered) 
    
sol = Solution()
sol.countCoveredBuildings(3, [[1,1],[1,2],[2,1],[2,2]])