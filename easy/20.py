def isValid(s: str) -> bool:
    if len(s) == 0:
        return True
    still_open=""
    closing = set([")", "]", "}"])
    oposing = {
        "(": ")",
        "[": "]",
        "{": "}"
    }
    for bracket in s:
        if len(still_open) == 0:
            if bracket in closing:
                return False

        if bracket not in closing:
            still_open += bracket
            continue


        if oposing.get(still_open[len(still_open) - 1]) != bracket:
            return False

        else:
            still_open = still_open[:-1]

    return len(still_open) < 1 

one = "()[]{}"
two = "([])"

isValid(two)