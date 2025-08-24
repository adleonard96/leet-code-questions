class Solution:
    def thousandSeparator(self, n: int) -> str:
        string_version = f"{n}"
        if len(string_version) <= 3:
            return string_version
        leading = len(string_version) % 3
        output = ""
        if leading > 0:
            output = string_version[:leading]
        for i in range(leading, len(string_version), 3):
            if len(output) > 0:
                output += "." + string_version[i:i+3]
            else:
                output += string_version[i:i+3]

        return output