class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        
        for c in s:
            curr_is_upper = c.isupper()
            last_val_upper = None
            if stack:
                last_val_upper = stack[-1].isupper()
            if stack and stack[-1].upper() == c.upper() and curr_is_upper != last_val_upper:
                stack.pop()
            else:
                stack.append(c)
        
        return "".join(stack)
    
Solution().makeGood("leEeetcode")