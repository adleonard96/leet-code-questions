def strStr(haystack: str, needle: str) -> int:
        found_index = -1
        current_needle = 0
        i = 0
        while i < len(haystack):
            if haystack[i] == needle[current_needle]:
                if found_index == -1:
                    found_index = i
                current_needle += 1
                if current_needle >= len(needle):
                    return found_index
            else:
                current_needle = 0
                if found_index != -1:
                    i = found_index
                found_index = -1
            i += 1
        
        if current_needle < len(needle):
            return -1
        return found_index

print(strStr("leetcode", "leeto"))