class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        dic = defaultdict(int)
        for jewel in jewels:
            dic[jewel] += 1

        for stone in stones:
            if stone in dic:
                count += 1

        return count