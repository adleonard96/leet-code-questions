class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        OPERATIONS = ["+", "-", "*", "/"]
        vals = []
        for token in tokens:
            if token in OPERATIONS:
                match token:
                    case "+":
                        val1 = vals.pop()
                        val2 = vals.pop()
                        vals.append(val1 + val2)
                    
                    case "*":
                        val1 = vals.pop()
                        val2 = vals.pop()
                        vals.append(val1 * val2)
                        
                    case "/":
                        val1 = vals.pop()
                        val2 = vals.pop()
                        vals.append(int(val2 / val1))

                    case "-":
                        val1 = vals.pop()
                        val2 = vals.pop()
                        vals.append(val2 - val1)
            else:
                vals.append(int(token))
                
        return vals[0]
    
sol = Solution()
print(sol.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
