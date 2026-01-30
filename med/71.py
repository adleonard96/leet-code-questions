class Solution:
    def simplifyPath(self, path: str) -> str:
        dirs = path.split('/')
        stack = []
        for dir in dirs:
            
            match (dir):

                case "..":
                    if stack: 
                        stack.pop()
                case "":
                    continue
                case ".":
                    continue
                case _:
                    stack.append(dir)
        
        stack = "/" + "/".join(stack)
        if stack and stack[-1] == "/" and len(stack) > 1:
            stack = stack[:-1]
            
        return stack
                    
print(Solution().simplifyPath("/home//foo/"))