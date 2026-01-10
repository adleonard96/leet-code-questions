class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        trip_map = defaultdict(str)

        for trip in paths:
            trip_map[trip[0]] = trip[1]

        for trip in paths:
            if trip[1] not in trip_map:
                return trip[1]