class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        right = len(s) - 1
        s_arr = list(s)
        for i in range(len(s_arr)):
            if s_arr[i].isalpha():
                while not s_arr[right].isalpha() and right > i:
                    right -= 1

                if right > i:
                    swap = s_arr[right]
                    s_arr[right] = s_arr[i]
                    s_arr[i] = swap
                    right -= 1

        s = "".join(s_arr)
        return s