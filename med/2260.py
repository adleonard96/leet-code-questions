class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        check = defaultdict(list)
        min_num = float("inf")
        found = False
        for i in range(len(cards)):
            if cards[i] in check:
                min_num = min(min_num, (i - check[cards[i]][-1]) + 1)
                found = True

            check[cards[i]].append(i)

        return min_num if found else -1