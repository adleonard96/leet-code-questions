def lengthOfLastWord(s: str) -> int:
    words = list(filter(lambda x: x != '', s.split(" ")))
    return len(words[-1])

word = "   fly me   to   the moon  "
lengthOfLastWord(word)