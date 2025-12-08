# class Solution:
#     def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
#         ans = []
#         lookup = {}
#         vals = sorted(list(set(temperatures)), reverse = True)

#         for i in range(len(temperatures)):
#             if temperatures[i] in lookup:
#                 lookup[temperatures[i]].append(i)
#             else:
#                 lookup[temperatures[i]] = [i]

#         for i in range(len(temperatures)):
#             current = temperatures[i]
#             larger = list(filter(lambda x: x > current, vals))
#             if len(larger) == 0:
#                 ans.append(0)
#                 continue
            
#             next_index = None

#             for num in larger:
#                 indx = 0
#                 while indx < len(lookup[num]):
#                     if lookup[num][indx] < i:
#                         lookup[num].pop(0)
#                     else:
#                         if not next_index:
#                             next_index = lookup[num][indx] - i
#                             if len(larger) == 1:
#                                 break
#                         else:
#                             if next_index > lookup[num][indx] - i:
#                                 next_index = lookup[num][indx] - i
#                                 break
#                             break
                            
#                         indx += 1
            
#             if next_index:
#                 ans.append(next_index)
#             else:
#                 ans.append(0)
            
#         return ans 
    
    
    
from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []  # Stack to keep track of indices
        result = [0] * len(temperatures)  # Initialize the result array with zeros
        for i, val in enumerate(temperatures):
            # While stack is not empty and current temperature is greater than
            # the temperature represented by the index at the top of the stack
            while stack and val > temperatures[stack[-1]]:
                index = stack.pop()  # Pop from stack
                result[index] = i - index  # Update the result
            stack.append(i)  # Add current temperature index to stack
        return result
    
Solution().dailyTemperatures([73,74,75,71,69,72,76,73])