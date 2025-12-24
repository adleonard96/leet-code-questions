class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        total_apples = sum(apple)
        capacity = sorted(capacity, reverse=True)
        count = 0
        for box in capacity:
            total_apples -= box
            count += 1
            if total_apples <= 0:
                return count