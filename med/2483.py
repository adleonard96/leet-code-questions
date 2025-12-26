class Solution:
    def bestClosingTime(self, customers: str) -> int:
        prefix = [1 if customers[0] == "Y" else -1]

        for i in range(1, len(customers)):
            if customers[i] == "Y":
                prefix.append(prefix[i - 1] + 1)
            else:
                prefix.append(prefix[i - 1] - 1)
        
        max_val = 0
        max_index = 0
        for i in range(len(prefix)):
            if prefix[i] > max_val:
                max_val = prefix[i]
                max_index = i

        return max_index + 1 if max_val > 0 else 0