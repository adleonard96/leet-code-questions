class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        start = 0
        current = 1
        end = 2
        count = 0

        if len(flowerbed) == 1:
            if flowerbed[0] == 0:
                return count+1 >= n

        if flowerbed[start] == 0 and flowerbed[current] == 0:
            flowerbed[start] = 1
            count += 1
            start += 1
            current += 1
            end += 1

        while end < len(flowerbed):
            if count == n:
                return True
            if flowerbed[start] != 0:
                start += 1
                current += 1
                end += 1
            elif flowerbed[current] != 0:
                start += 1
                current += 1
                end += 1
            elif flowerbed[end] != 0:
                start = end
                current = end + 1
                end += 2
            else:
                flowerbed[current] = 1
                start = end
                current = end + 1
                end += 2
                count += 1

        if flowerbed[-1] == 0 and flowerbed[-2] == 0:
            count += 1

        return count >= n