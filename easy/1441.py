class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ans = []
        pos = 0
        for i in range(1, n + 1):
            if pos >= len(target):
                return ans
            ans.append("Push")
            if target[pos] == i:
                pos += 1
                continue
            ans.append("Pop")
        return ans