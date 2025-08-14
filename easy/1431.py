class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max = list(sorted(candies, reverse=True))[0]
        greatest = []
        for i in range(len(candies)):
            greatest.append(candies[i] + extraCandies >= max)

        return greatest