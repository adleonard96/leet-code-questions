class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        for i, val in enumerate(heights):
            stack.append(val)
            while stack and val > stack[0] or i+1 == len(heights) and stack:
                if len(stack) * stack[-2] > max_area:
                    max_area = len(stack) * stack[-2]
                stack.pop()
            stack.append(val)

        return max_area
    
Solution().largestRectangleArea([2,1,5,6,2,3])