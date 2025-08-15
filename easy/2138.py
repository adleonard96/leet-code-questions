class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        split = []
        for i in range(0, len(s), k):
            split.append(s[i:i+k])

        if len(split[-1]) < k:
            split[-1] += fill * (k - len(split[-1]))

        return split