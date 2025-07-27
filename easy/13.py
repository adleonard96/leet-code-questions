class Solution:

    def romanToInt(self, s: str) -> int:
        last_letter = ""
        current_value = 0
        for i in range(len(s)):
            if last_letter == "":
                last_letter = s[i]
                current_value += get_value(s[i]) 
                continue

            if last_letter == s[i] or get_value(last_letter) > get_value(s[i]):
                current_value += get_value(s[i]) 
                last_letter = s[i]
            else:
                current_value -= get_value(last_letter)
                current_value -= get_value(last_letter)
                current_value += get_value(s[i]) 
                last_letter = s[i]
                

        return current_value

def get_value(s: str) -> int:
    match s:
        case "I":
            return 1
        case "V":
            return 5
        case "X":
            return 10
        case "L":
            return 50
        case "C":
            return 100
        case "D":
            return 500
        case "M":
            return 1000
    