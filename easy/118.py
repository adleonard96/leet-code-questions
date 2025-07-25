class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for i in range(numRows):
            if len(res) == 0:
                res.append([1])
                continue

            new_section = []
            for j in range(len(res[i - 1])):
                if j == 0:
                    new_section.append(res[i - 1][j])
                else:
                    new_section.append(res[i - 1][j] + res[i - 1][j - 1])
            
            new_section.append(1)
            res.append(new_section)

        return res
