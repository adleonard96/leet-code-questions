class Solution:
    def countElements(self, arr: List[int]) -> int:
        unique = set(arr)
        count = 0
        for elem in arr:
            if elem + 1 in unique:
                count += 1

        return count