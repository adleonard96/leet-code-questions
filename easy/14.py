class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest_so_far = strs[0]
        current = ""
        for i in range(1, len(strs)):
            if longest_so_far == "":
                return ""

            for current_char in range(len(strs[i])):
                if current_char >= len(longest_so_far):
                    break
                elif strs[i][current_char] == longest_so_far[current_char]:
                    current += strs[i][current_char]
                else:
                    break

            longest_so_far = current
            current = ""

            

        return longest_so_far 
    
sol = Solution()
sol.longestCommonPrefix(["flower","flow","flight"])