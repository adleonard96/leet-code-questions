class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        max_val = 0

        for val in strs:
            try:
                if max_val < int(val):
                    max_val = int(val)
            except:
                if max_val < len(val):
                    max_val = len(val)
        
        return max_val