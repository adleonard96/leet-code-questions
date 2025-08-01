class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        sneaky = []
        visited = {}

        for num in nums:
            if len(sneaky) == 2:
                return sneaky

            if num in visited:
                sneaky.append(num)
            else:
                visited[num] = num
        
        return sneaky